import os, sys
import pandas as pd

odir = os.path.join(os.getcwd(), 'analysis')

filename = '20180414_analysis_calendar.csv'
df = pd.read_csv(os.path.join(odir, filename))
df['month'] = [str(i).zfill(2) for i in df['month']]
df['combo'] = [eval(i) for i in df['combo']]


# print(df.iloc[0]['combo'])
# 
# return(0)

     
for k,v in df.groupby(['profile','month']):
    for idx, row in v.iterrows():
        print(row['combo'], type(row['combo']), row['combo'][0])
#     
#     print(type(v), type(v['combo']))
#     print(v.iloc[0]['combo'])
#     print(v['combo'])
    
#     print(k, v['combo'], v['mean'].mean(), v['std'].mean())
 
     
# 
# import statsmodels.api as sm
# 
# 
# import importlib
# importlib.reload(PyShare.SpPlot)
# importlib.reload(PyShare.Analysis)
# 
# PyShare.SpPlot.spboxplot(result2, title, ylabel, annotation, value['month_list'][0])
# 
# # result_log = result2.copy()
# # for k, v in result2.items():
# #     result_log.update({k:v.diff(1).dropna()})
# # 
# # PyShare.SpPlot.spboxplot(result_log, title, value['month_list'][0])
# 
# 
# x=[1,2,3,4,5,6,7]
# pd.rolling_mean(pd.DataFrame(x),window=3)
# pd.DataFrame(x).rolling(window=3).mean()


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
