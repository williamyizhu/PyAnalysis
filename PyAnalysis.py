import os
import sys
import pandas as pd
import numpy as np
import datetime as dt
import argparse
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\PyShare'))
import Utils
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\SpreadAnalysis'))
import Analysis
import SpPlot

'''
std shift, calculate std for each leg
term structure curve slope change pic
'''

def func(args):
#     ------------- parse command line input args -------------
#     default use wind datasource
    underlying_config_file = list() if args.underlying_config_file is None else args.underlying_config_file[0].lower()
    profile_list = list() if args.profile is None else [x.upper() for x in args.profile]
    exchange_list = list() if args.exchange is None else [x.upper() for x in args.exchange]    
    underlying_list = list() if args.underlying is None else [x.upper() for x in args.underlying]
    combo_type = list() if args.combo_type is None else [x.upper() for x in args.combo_type]    
    ts_diff = 0 if args.ts_diff is None else int(args.ts_diff[0])
    ex_outlier_thres = 3.5 if args.ex_outlier_thres is None else float(args.ex_outlier_thres[0])
    x_std = [1.96] if args.x_std is None else [float(i) for i in args.x_std]

#     --------------- prepare data ---------------
#     directory for symbol data csv file
#     fdir = 'C:\\wind_data_cn_futures\\eod_c\\'
    fdir = 'C:\\quandl_data_cn_futures\\eod\\'

#     underlying configuration file
    underlying_dict = Utils.config_read(underlying_config_file)
    for key, value in underlying_dict.items():
        value['ratio'] = [int(i) for i in value['ratio']]
        value['exchange'] = [i.split('.')[0] for i in value['exul']]
        value['underlying'] = [i.split('.')[1] for i in value['exul']]
        value['merge_col'] = ['DATETIME']
        value['obs_col'] = ['OPEN', 'CLOSE']

#     select specific profile, exchange, underlying, combo_type
    if len(profile_list) != 0:
        underlying_dict = {key: value for key, value in underlying_dict.items() if key in profile_list}
    if len(exchange_list)!=0:
        underlying_dict = {key: value for key, value in underlying_dict.items() if any(ii in exchange_list for ii in value['exchange'])}
    if len(underlying_list)!=0:
        underlying_dict = {key: value for key, value in underlying_dict.items() if any(ii in underlying_list for ii in value['underlying'])}
    if len(combo_type) != 0:
        underlying_dict = {key: value for key, value in underlying_dict.items() if any(ii in combo_type for ii in value['combo_type'])}

#     calculate year and month combination
    for key, value in underlying_dict.items():
        if len(value['exul']) == len(value['month']) == len(value['ratio']):
            year = list(range(int(value['year'][0]), int(value['year'][1])))
#             value['exul'] = ['DCE.M', 'DCE.M']
#             value['month'] = 01;05;09,05;09;01+1
#             month_expr = [[['01'], ['05'], ['09']], [['05'], ['09'], ['01', '1']]]
#             month = [['01', '05', '09'], ['05', '09', '01']] --> [['01', '05'], ['05', '09'], ['09', '01']]
#             year_shift = [[0, 0, 0], [0, 0, 1]] --> [[0, 0], [0, 0], [0, 1]]
            month = []
            year_shift = []
            month_expr = [[s.split('+') for s in m.split(';')] for m in value['month']]
            for ms in month_expr:
                month.append([i[0] for i in ms])
                year_shift.append([0 if len(i)==1 else int(i[1]) for i in ms])
            value['front_month'] = month[0]
#             transform list structure
            month = pd.DataFrame(month).T.values.tolist()
            year_shift = pd.DataFrame(year_shift).T.values.tolist()
#             create combo_list = [['DCE.M1201', 'DCE.M1205'], ['DCE.M1205', 'DCE.M1209'], ['DCE.M1209', 'DCE.M1301'], ['DCE.M1301', 'DCE.M1305']]
            combo_list = []
            for yy in year:
                for m,ys in zip(month,year_shift):
                    yy2 = [str(yy+i)[2:] for i in ys]
                    combo_list.append([''.join([i,j,k]) for i,j,k in zip(value['exul'],yy2,m)])
            value['combo_list'] = combo_list
        else:
            print('profile configuration may contain error:', key, value)

#     Analysis.combo_analysis, Analysis.combo_stats, SpPlot.spboxplot, spread plot
#     result = dict({('CZCE.CF1401','CZCE.CF1405'):[value], ('CZCE.CF1405','CZCE.CF1409'):[value]})
    watchlist = dict()
    for x in x_std:
        watchlist.update({x:[]})
    for key,value in underlying_dict.items():
#         --------------- analysis ---------------
#         calculate spread value for all combo in the value['combo_list'], check if to use the time series difference on the result data
        result = Analysis.combo_analysis(fdir, value['combo_list'], value['ratio'], value['merge_col'][0], int(value['last_day_shift'][0]), value['obs_col'])
        if ts_diff>0:
            for k, v in result.items():
                result.update({k:v.diff(ts_diff).dropna()})

#         calculate statistics for all combo, local and global, save data in watchlist
        sloc, sglb = Analysis.combo_stats(result, ex_outlier_thres)
        for k, v in result.items():
            if Analysis.is_contract_expired(k[0]):
                for x in x_std:
                    if v.iloc[-1] < sloc[k]['mean']-x*sglb['std'] or sloc[k]['mean']+x*sglb['std'] < v.iloc[-1]:
                        watchlist[x].append([key, k, v.iloc[-1]])

#         --------------- spread plot ---------------
#         check if png output directory exists
        odir = os.path.join(os.getcwd(), value['combo_type'][0])    
        if not os.path.exists(odir):
            os.makedirs(odir)

#         analysis result for specific front month combo, '00' means include all front month combo
        for month_value in value['front_month']+['00']:
#             only selection front month contract, which is in the month_value
            if month_value=='00':
                result2 = result.copy()
            else:
                result2 = {}
                for xkey, xvalue in result.items():   
                    if xkey[0].split('.')[1][-2:]==month_value:
                        result2.update({xkey:xvalue})                

#             result2 dict may be empty, e.g., SHFE.AU butterfly, can not trade such ratio, i.e., no data
            if len(result2)==0:
                print(key, month_value, 'does not have sufficient data for such ratio')
                continue

#             boxplot and save figure to png
            title = 'date=' + dt.datetime.today().strftime('%Y-%m-%d') + \
                    ' lds=' + value['last_day_shift'][0] + \
                    ' tsdiff=' + str(ts_diff) + \
                    ' mean=' + str(sglb['mean']) + \
                    ' std=' + str(sglb['std']) + \
                    ' eos=' + str(ex_outlier_thres)
            ylabel = key + ' ratio=' + str(value['ratio']) + ' front_month=' + month_value
            annotation = [str(len(v))+'\n'+str(sloc[k]['outlier']) for k,v in result2.items()]                                
            figname = os.path.join(odir, '.'.join([value['asset_class'][0],key,month_value,'png']))    
            SpPlot.spboxplot(result2, title, ylabel, annotation, value['front_month'][0], figname)

            print(ylabel, title)
            [print(k) for k in result2.keys()]

    print('--------------- watchlist ---------------')
    odir = os.path.join(os.getcwd(), 'watchlist')    
    if not os.path.exists(odir):
        os.makedirs(odir)
    f = open(os.path.join(odir, '.'.join([underlying_config_file.split('.')[0],'txt'])), 'w')
    for k, v in watchlist.items():
        print('x_std:', k)
        [print(i) for i in v]
        f.write(''.join(['x_std:', str(k), '\n']))
        [f.write(str(i)+'\n') for i in v]
    f.close()

def main():
    parser = argparse.ArgumentParser(usage='Analysis')
    parser.add_argument('-ucf', '--underlying_config_file', nargs='*', action='store')
    parser.add_argument('-p', '--profile', nargs='*', action='store')
    parser.add_argument('-e', '--exchange', nargs='*', action='store')    
    parser.add_argument('-u', '--underlying', nargs='*', action='store')    
    parser.add_argument('-ct', '--combo_type', nargs='*', action='store')
    parser.add_argument('-tsdiff', '--ts_diff', nargs='*', action='store')
    parser.add_argument('-ex', '--ex_outlier_thres', nargs='*', action='store')
    parser.add_argument('-xs', '--x_std', nargs='*', action='store')    
    args = parser.parse_args()    
#     print(args)
    try:
        func(args)
    except Exception as e: 
        print(__file__, '\n', e)  

if __name__ == '__main__':
    main()

# cd 'Z:\williamyizhu On My Mac\Documents\workspace\PyAnalysis'
# cd 'Z:\Documents\workspace\PyAnalysis'

# python .\PyAnalysis.py -ucf underlying.ini -r cs bf -tsdiff 0 -ex 5
# python .\PyAnalysis.py -ucf underlying.ini -e shfe -u cu -r bf -tsdiff 0 -ex 5

# -ucf, underlying_config_file
# -p, profile name in underlying_config_file
# -e, select specific exchange from the config file
# -u, select specific underlying
# -ct, combo_type, e.g., CS, BF, ICS, BX
# -tsdiff, time series differential
# -ex, excluding outlier threshold, default value = 3.5
# -xs, combo outside [mean +/- x_std * std] will be saved in watch list