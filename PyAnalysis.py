import os
import sys
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\SpreadAnalysis'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\PyShare'))
import pandas as pd
import datetime as dt
import argparse
import Utils
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
    eval_date = dt.datetime.now() if args.eval_date is None else dt.datetime.strptime(args.eval_date[0], '%Y%m%d')
    profile_list = list() if args.profile is None else [x.upper() for x in args.profile]
    exchange_list = list() if args.exchange is None else [x.upper() for x in args.exchange]    
    underlying_list = list() if args.underlying is None else [x.upper() for x in args.underlying]
    combo_type = list() if args.combo_type is None else [x.upper() for x in args.combo_type]    
    ts_diff = 0 if args.ts_diff is None else int(args.ts_diff[0])
    ex_outlier_thres = 3.5 if args.ex_outlier_thres is None else float(args.ex_outlier_thres[0])

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

#     Analysis.combo_analysis, group in expiration months, SpPlot.spboxplot
    exportlist = []
    for key,value in underlying_dict.items():
        print('--------', key, '--------')

#         --------------- calculate spread value, local stats analysis ---------------
#         calculate spread value for all combo in the value['combo_list'], check if to use the time series difference on the result data
#         result = dict({('CZCE.CF1401','CZCE.CF1405'):[value], ('CZCE.CF1405','CZCE.CF1409'):[value]})
#         stats = dict({('CZCE.CF1401','CZCE.CF1405'):{'mean':value, 'std':value, ...}, ('CZCE.CF1405','CZCE.CF1409'):{'mean':value, 'std':value, ...}})
        result, stats = Analysis.combo_analysis(fdir, value['combo_list'], value['merge_col'][0], eval_date, int(value['last_day_shift'][0]), value['obs_col'], value['ratio'], ex_outlier_thres)

#         --------------- analysis based on expiration months, spread plot ---------------
#         check if png output directory exists
        odir = os.path.join(os.getcwd(), value['combo_type'][0])    
        if not os.path.exists(odir):
            os.makedirs(odir)

#         sub group analysis result for specific front month combo, '00' means include all front month combo
        for month_value in value['front_month']+['00']:
#             only selection front month contract for both result and stats, calculate statistics for sub group
#             stats2 is the local stats in sub group (e.g., month_value='01'), stats2g is the global statistics value of that sub group
            if month_value=='00':
                result2 = result.copy()
                stats2 = stats.copy()
            else:
                result2 = {}
                stats2 = {}
                for xkey, xvalue in result.items():   
                    if xkey[0].split('.')[1][-2:]==month_value:
                        result2.update({xkey:xvalue})
                        stats2.update({xkey:stats[xkey]})
            stats2g = Analysis.combo_global_stats(stats2)

#             result2 dict may be empty, e.g., SHFE.AU butterfly, can not trade such ratio, i.e., no data
            if len(result2)==0:
                print(key, month_value, 'does not have sufficient data for such ratio')
                continue

#             --------------- save key statistics to list, later export to csv file ---------------
            for k, v in result2.items():
                tmp = [stats2[k]['last_trading_day'], stats2[k]['outlier'], stats2[k]['n'], stats2[k]['mean'], stats2[k]['median'], stats2[k]['std']]
                exportlist.append([key, month_value, k, *tmp, v.iloc[-1]])

#             --------------- boxplot and save figure to png ---------------
#             *** red line (mean value) in the figure may not be the same as mean value in title ***
#             *** combo_global_stats() excludes entries with less than 30 observations, SpPlot() does not***
            title = 'date=' + eval_date.strftime('%Y-%m-%d') + \
                    ' lds=' + value['last_day_shift'][0] + \
                    ' mean=' + str(stats2g['mean']) + \
                    ' std=' + str(stats2g['std']) + \
                    ' eos=' + str(ex_outlier_thres)
            ylabel = key + ' ratio=' + str(value['ratio']) + ' front_month=' + month_value
            annotation = [str(len(v))+'\n'+str(stats[k]['outlier']) for k,v in result2.items()]                                
            figname = os.path.join(odir, '.'.join([value['asset_class'][0],key,month_value,'png']))
            SpPlot.spboxplot(result2, title, ylabel, annotation, value['front_month'][0], figname)
            print(ylabel, title)
#             [print(k) for k in result2.keys()]

#     --------------- export key statstics to csv file ---------------
    odir = os.path.join(os.getcwd(), 'analysis')
    if not os.path.exists(odir):
        os.makedirs(odir)
    fd = pd.DataFrame.from_records(exportlist, columns=['profile','month','combo','last_trading_day','outlier','n','mean','median','std','last_value'])
    filename = '.'.join([eval_date.strftime('%Y%m%d_analysis_')+underlying_config_file.split('.')[0], 'csv'])
    fd.to_csv(os.path.join(odir, filename), index=False)

def main():
    parser = argparse.ArgumentParser(usage='Calculate combination value based on underlying config file')
    parser.add_argument('-ucf', '--underlying_config_file', nargs='*', action='store', help='underlying configuration file')
    parser.add_argument('-d', '--eval_date', nargs='*', action='store', help='evaluation date')
    parser.add_argument('-p', '--profile', nargs='*', action='store', help='profile name in underlying configuration file')
    parser.add_argument('-e', '--exchange', nargs='*', action='store', help='select specific exchange from configuration file')
    parser.add_argument('-u', '--underlying', nargs='*', action='store', help='select specific underlying')
    parser.add_argument('-ct', '--combo_type', nargs='*', action='store', help='combo_type, e.g., CS, BF, ICS, BX')
    parser.add_argument('-tsdiff', '--ts_diff', nargs='*', action='store', help='time series differential')
    parser.add_argument('-ex', '--ex_outlier_thres', nargs='*', action='store', help='excluding outlier threshold, default value = 3.5')
    args = parser.parse_args()    
#     print(args)
    try:
        func(args)
    except Exception as e:
        print(__file__, '\n', e)

if __name__ == '__main__':
    main()

# cd 'Z:\Documents\workspace\PyAnalysis'

# python .\PyAnalysis.py -ucf calendar.ini -tsdiff 0 -ex 5
# python .\PyAnalysis.py -ucf butterfly.ini -tsdiff 0 -ex 5
# python .\PyAnalysis.py -ucf combo.ini -tsdiff 0 -ex 5

#         if ts_diff>0:
#             for k, v in result.items():
#                 result.update({k:v.diff(ts_diff).dropna()})
#         print('------------', len(result), [len(v) for v in result.values()])