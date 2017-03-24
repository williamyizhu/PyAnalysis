[DCE.I_SHFE.RB]
asset_class = FERR
ExUL = DCE.I,SHFE,RB
year_start = 2012
month_list = 01;05;09,01;05;10
ratio = 1;-1,-1;1
last_day_shift = -30

[DCE.I_DCE.J_SHFE.RB]
asset_class = FERR
ExUL = DCE.I,DCE.J,SHFE,RB
year_start = 2012
month_list = 01;05;09,01;05;09,01;05;10
ratio = 5,1,-1
last_day_shift = -30

import os
import PyShare.Utils

os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyAnalysis')

# underlying configuration file
underlying_dict = PyShare.Utils.config_read('inter_commodity.ini')    

    for key, value in underlying_dict.items():
#         value['exchange'] = key.split('.')[0]
#         value['underlying'] = key.split('.')[1]
        value['merge_col'] = 'DATETIME'
        value['obs_col'] = ['OPEN', 'CLOSE']
        
        if len(value['exul'])==len(value['month_list'])==len(value['ratio']):
            print('OK')
            
            [i.split(';') for i in value['month_list']]
            [int(i) for i in value['ratio']]
            
        else:
            print('...')
#         value[]
        
        

'DCE.M'
['01','05','09']
'CZCE.RM'
['01','05','09']
[1,-1]
[1,-1,-1,1]

'DCE.I'
['01','05','09']
'SHFE.RB'
['01','05','10']
[6,-1]
[6,-6,-1,1]

import statsmodels.api as sm


key = 'DCE.M'
value = underlying_dict[key]


def xyz(x, y=None, z=3):
    if y==None:
        print('abc',y)
    else:
        print(y)

xyz(1,z=5)

gg = list()
gg=[gg+v for v in result.values()]

import importlib
importlib.reload(PyShare.SpPlot)
importlib.reload(PyShare.Analysis)

PyShare.SpPlot.spboxplot(result2, title, ylabel, annotation, value['month_list'][0])

# result_log = result2.copy()
# for k, v in result2.items():
#     result_log.update({k:v.diff(1).dropna()})
# 
# PyShare.SpPlot.spboxplot(result_log, title, value['month_list'][0])


x=[1,2,3,4,5,6,7]
pd.rolling_mean(pd.DataFrame(x),window=3)
pd.DataFrame(x).rolling(window=3).mean()
# ------------------------------- test -------------------------------
result2

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
            
PyShare.Analysis.combo_list(fdir, 'DCE', 'M', 2015, ['01','05','09'], 2)

Analysis.combo_list(fdir, 'CZCE', 'ZC', ['01','05','09'], 2)


{'DCE.I':{'year_start':2012, 'month_list':['01','05','09']}}
{'SHFE.RB':{'year_start':2012, 'month_list':['01','05','10']}}

[1,-1,1,-1]

[['DCE.M0505', 'DCE.M0509', 'DCE.Y0505', 'DCE.Y0509'], ]

[['DCE.M0501', 'DCE.M0505'], ['DCE.M0505', 'DCE.M0509'], ['DCE.M0509', 'DCE.M0601']]
[                            ['DCE.Y0505', 'DCE.Y0510'], ['DCE.Y0509', 'DCE.Y0601']]

PyShare.Analysis.is_outlier(v, pmedian=94.5, thres=1)

# --------------- test ---------------
import Analysis
fdir = 'C:\\wind_data_cn_futures\\eod\\'

result = {}
combo = ['DCE.M1605','DCE.M1609','DCE.M1701']
combo = ['DCE.M1601','DCE.M1605','DCE.M1609']
combo = ['CZCE.ZC701','CZCE.ZC705','CZCE.ZC709']
combo = ['CZCE.ZC705','CZCE.ZC709','CZCE.ZC801']

# combo_list = Analysis.combo_list(fdir, 'SHFE', 'CU', ['01','05','09'], 3)
# for i in combo_list:
#     print(i)

# select contract file and merge into a dataframe
df = Analysis.merge_csv(fdir, combo, 'DATETIME', 30)
     
# select column used for analysis, drop rows which contains any NaN value
mg = Analysis.concat(df, ['OPEN', 'CLOSE'])
     
# apply ratio calculation, e.g., box=[1,-1,1,-1], butterfly=[1,-2,-1]
sg = Analysis.ratio(mg, [1,-2,1])
     
result.update({tuple(combo):sg['result']})


# mu, sigma = 100, 15
# add a 'best fit' line
# y = mlab.normpdf( bins, mu, sigma)
# l = plt.plot(bins, y, 'r--', linewidth=1)


# mc = sm.OLS(sg['result'])
# mc = sm.OLS(sg.iloc[:,1])
# sg.iloc[:,0]

# mc = sm.OLS(sg.iloc[:,0], sm.add_constant(sg.iloc[:,1]))
# results = mc.fit()
# print(results.summary())
# 
# import matplotlib.pyplot as plt
# plt.hist(results.resid)
