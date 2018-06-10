import os
import sys
import pandas as pd
import numpy as np
import datetime as dt
import argparse
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\SpreadAnalysis'))
import Analysis

def func(args):
#     ------------- parse command line input args -------------
#     default use wind datasource
    underlying_config_file = list() if args.underlying_config_file is None else args.underlying_config_file[0].lower()
    eval_date = dt.datetime.now() if args.eval_date is None else dt.datetime.strptime(args.eval_date[0], '%Y%m%d')
    x_std = [1.96] if args.x_std is None else [float(i) for i in args.x_std]
    selection_criteria = 'mr' if args.selection_criteria is None else args.selection_criteria[0].lower()

#     --------------- watchlist selection criteria ---------------
#     import csv file, following code can be run separately, need to specify filename
    odir = os.path.join(os.getcwd(), 'analysis')
    filename = '.'.join([eval_date.strftime('%Y%m%d_analysis_')+underlying_config_file.split('.')[0], 'csv'])
    df = pd.read_csv(os.path.join(odir, filename))
    df['month'] = [str(i).zfill(2) for i in df['month']]
    df['combo'] = [eval(i) for i in df['combo']]

#     skip selection process if any of the following situation occurs
#     1. eval_date is in delivery month of the contract, i.e., eval_date is on or after 1st day of delivery month
#     2. *** if last_trading_day is too far ahead of eval_date, not implement yet ***
#        *** weekend or long holiday may also cause the last_trading_day is too far ahead of eval_date ***
    watchlist = dict()
    tlist = ['last_trading_day','profile','month','combo','mean','std','last_value','lower_range','upper_range','buy_sell']
    for x in x_std:
        watchlist.update({x:pd.DataFrame(columns=tlist)})
#     gpdf.columns = df.columns = ['profile','month','combo','last_trading_day','outlier','n','mean','median','std','last_value']
#     gpk = ['profile','month']
    for gpk, gpdf in df.groupby(['profile','month']):
#         calculate average mean and std for sub group
        gpmean = gpdf['mean'].mean()
        gpstd = gpdf['std'].mean()
        for idx, row in gpdf.iterrows():
            if Analysis.is_contract_in_deliver_month(row['combo'][0], eval_date):
                pass
            else:
                for x in x_std:
#                     selection criteria, row['mean'] is moving average
                    lower_range = row['mean'] - x * gpstd
                    upper_range = row['mean'] + x * gpstd
                    vlist = [row['last_trading_day'], *gpk, row['combo'], row['mean'], gpstd, row['last_value'], lower_range, upper_range]
#                     append result to watchlist
                    if selection_criteria == 'mr':
                        sc_indicator = 'meanreverting'
                        if row['last_value'] < lower_range:
                            vlist = vlist + ['BUY']
                            watchlist[x] = watchlist[x].append(dict(zip(*[tlist, vlist])), ignore_index=True)
                        elif row['last_value'] > upper_range:
                            vlist = vlist + ['SELL']
                            watchlist[x] = watchlist[x].append(dict(zip(*[tlist, vlist])), ignore_index=True)
                    elif selection_criteria == 'bo':
                        sc_indicator = 'breakout'
                        if lower_range <= row['last_value'] <= upper_range:
                            vlist = vlist + ['BREAKOUT']
                            watchlist[x] = watchlist[x].append(dict(zip(*[tlist, vlist])), ignore_index=True)                        
                    else:
                        print('unknown selectioin criteria:', selection_criteria)

    print('--------------- watchlist ---------------')
#     watchlist file, e.g., 20180515_watchlist_butterfly_meanreverting
    fftmp = '_'.join([eval_date.strftime('%Y%m%d'), 'watchlist', underlying_config_file.split('.')[0], sc_indicator])

#     watchlist summary for all x_std, for daily reporting purpose
    odir = os.path.join(os.getcwd(), 'watchlist')
    if not os.path.exists(odir):
        os.makedirs(odir)
    f = open(os.path.join(odir, '.'.join([fftmp, 'txt'])), 'w')
#     iterate through watchlist over different x_std, v is dataframe
    for k, v in watchlist.items():
        print('x_std:', k)
        f.write(''.join(['x_std:', str(k), '\n']))
        d = v.to_dict('index')
        for kk, vv in d.items():
            print(vv)
            f.write(str(vv)+'\n')
    f.close()

#     create watchlist folder for x_std, export dataframe to csv file, used in back testing
    for k, v in watchlist.items():
        odir = os.path.join(os.getcwd(), 'watchlist', '_'.join([sc_indicator,'x_std',str(k)]))
        if not os.path.exists(odir):
            os.makedirs(odir)
        v.to_csv(os.path.join(odir, '.'.join([fftmp, 'csv'])), index=False)

def main():
    parser = argparse.ArgumentParser(usage='Create watchlist')
    parser.add_argument('-ucf', '--underlying_config_file', nargs='*', action='store', help='underlying configuration file')
    parser.add_argument('-d', '--eval_date', nargs='*', action='store', help='evaluation date')
    parser.add_argument('-xs', '--x_std', nargs='*', action='store', help='combo outside/inside [mean +/- x_std * std] will be saved in watch list')
    parser.add_argument('-sc', '--selection_criteria', nargs='*', action='store', choices=['mr','bo'], help='selection criteria, mr:meanreverting, bo:breakout')
    args = parser.parse_args()
#     print(args)
    try:
        func(args)
    except Exception as e:
        print(__file__, '\n', e)

if __name__ == '__main__':
    main()

# cd 'Z:\Documents\workspace\PyAnalysis'

# python .\PyWatchlist.py -ucf calendar.ini -xs 1.5 1.95 2.5
# python .\PyWatchlist.py -ucf butterfly.ini -xs 1.5 1.95 2.5
# python .\PyWatchlist.py -ucf combo.ini -xs 1.5 1.95 2.5

# python .\PyWatchlist.py -ucf calendar.ini -xs 0.2 0.5 -sc bo
# python .\PyWatchlist.py -ucf butterfly.ini -xs 0.2 0.5 -sc bo
# python .\PyWatchlist.py -ucf combo.ini -xs 0.2 0.5 -sc bo

# python .\PyWatchlist.py -ucf combo.ini -d 20180415 -xs 1.5 1.95 2.5
