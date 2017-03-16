import os
import sys
import pandas as pd
import numpy as np
import functools
import argparse
mpath = os.path.join(os.path.abspath('..'), 'PyShare')
sys.path.append(mpath)
import PyShare.Analysis
import PyShare.SpPlot
import PyShare.Utils

'''
inter-commodity list
return v.s. return, time diff
'''

# wdir = 'Z:\williamyizhu On My Mac\Documents\workspace\PyAnalysis'
# os.chdir(wdir)
# underlying_config_file = 'underlying_sample.ini'
# ratio = ['cs']
# ts_diff = 0
# ex_outlier_thres = 3.5

def func(args):
#     ------------- parse command line input args -------------
#     default use wind datasource
    underlying_config_file = [] if args.underlying_config_file is None else args.underlying_config_file[0].lower()
    ratio = ['cs','bf'] if args.ratio is None else [x.lower() for x in args.ratio]    
    ts_diff = 0 if args.ts_diff is None else int(args.ts_diff[0])
    ex_outlier_thres = 3.5 if args.ex_outlier_thres is None else float(args.ex_outlier_thres[0])

#     --------------- prepare data ---------------
#     directory for symbol data csv file
    fdir = 'C:\\wind_data_cn_futures\\eod_c\\'  

#     underlying configuration
    underlying_dict = PyShare.Utils.config_read(underlying_config_file)    
    for key, value in underlying_dict.items():
        value['exchange'] = key.split('.')[0]
        value['underlying'] = key.split('.')[1]
        value['merge_col'] = 'DATETIME'
        value['obs_col'] = ['OPEN', 'CLOSE']   
            
#     ratio for analysis
    ratio_dict = dict()
    for i in ratio:   
        if i=='cs':
            ratio_dict.update({'calendar':[1,-1]})
        elif i=='bf':
            ratio_dict.update({'butterfly':[1,-2,1]})
        elif i=='bx':
            ratio_dict.update({'box':[1,-1,-1,1]})        

#     --------------- run analysis ---------------
    for ratio_key, ratio_value in ratio_dict.items():
#         check if png output directory exists
        odir = os.path.join(os.getcwd(), ratio_key)    
        if not os.path.exists(odir):
            os.makedirs(odir)
    
#         ratio_value is ratio_list, analysis result for all combo
        for key, value in underlying_dict.items():        
#             create a list of all the combo list, e.g., 
#             [['SHFE.RB1201', 'SHFE.RB1205'], ['SHFE.RB1205', 'SHFE.RB1210'], ...]
#             [['SHFE.RB1201', 'SHFE.RB1205', 'SHFE.RB1210'], ['SHFE.RB1205', 'SHFE.RB1210', 'SHFE.RB1301'], ...]
            moving_window = len(ratio_value)        
            combo_all = PyShare.Analysis.combo_list(fdir, value['exchange'], value['underlying'], int(value['year_start'][0]), value['month_list'], moving_window)  
            
#             calculate the spread value for all combo
            result = PyShare.Analysis.combo_analysis(fdir, combo_all, ratio_value, value['merge_col'], int(value['last_day_shift'][0]), value['obs_col'])
    
#             if convert to use the difference on the result data
            if ts_diff>0:
                for k, v in result.items():
                    result.update({k:v.diff(ts_diff).dropna()})
    
#             analysis result for specific front month combo, '00' means include all front month combo
            for month_value in value['month_list']+['00']:
#                 only selection front month contract, which is in the month_value
                if month_value=='00':
                    result2 = result.copy()
                else:
                    result2 = {}
                    for xkey, xvalue in result.items():   
                        if xkey[0].split('.')[1][-2:]==month_value:
                            result2.update({xkey:xvalue})                
                
#                 exclude outliers, pmedian=None, uses local median, instead of global median
                outlier_idx = {}
                pm = functools.reduce(lambda x,y: pd.concat([x,y],ignore_index=True), result2.values())
                for k, v in result2.items():
                    idx = PyShare.Analysis.is_outlier(v, pmedian=pm.median(), thres=ex_outlier_thres)
#                     idx = PyShare.Analysis.is_outlier(v, pmedian=None, thres=ex_outlier_thres)                
                    result2.update({k:v[~idx]})
                    outlier_idx.update({k:idx})
                 
#                 boxplot and save figure to png
                title = 'lds=' + value['last_day_shift'][0] + \
                        ' tsdiff=' + str(ts_diff) + \
                        ' median=' + str(pm.median()) + \
                        ' eos=' + str(ex_outlier_thres)
                ylabel = key + ' ratio=' + str(ratio_value) + ' front_month=' + month_value            
                annotation = [str(len(v))+'\n'+str(list(outlier_idx[k]).count(True)) for k,v in result2.items()]                                
                figname = os.path.join(odir, '.'.join([key,month_value,'png']))    
                PyShare.SpPlot.spboxplot(result2, title, ylabel, annotation, value['month_list'][0], figname)
                 
                print(ylabel, title)
                for k in result2.keys():
                    print(k) 

def main():
    parser = argparse.ArgumentParser(usage='Analysis')
    parser.add_argument('-ucf', '--underlying_config_file', nargs='*', action='store')
    parser.add_argument('-r', '--ratio', nargs='*', action='store')
    parser.add_argument('-tsdiff', '--ts_diff', nargs='*', action='store')
    parser.add_argument('-ex', '--ex_outlier_thres', nargs='*', action='store')
    args = parser.parse_args()    
#     print(args)
    try:
        func(args)
    except Exception as e: 
        print(__file__, '\n', e)  
 
if __name__ == '__main__':
    main()
    
# .\PyAnalysis.py -ucf underlying.ini -r cs bf -tsdiff 0 -ex 5
# -m, mode, how to generate combo_all, i.e., same underlying or inter-underlying
# -ucf, underlying_config_file
# -r, ratio, e.g., cs, bf, bx
# -tsdiff, time series differential
# -ex, excluding outlier threshold, default value = 3.5