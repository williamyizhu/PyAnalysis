import os
import configparser

os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyAnalysis')
os.getcwd()

# # -------------- params.ini --------------
# params = configparser.SafeConfigParser()
# 
# # Wind, WSET, future exchange all trading contracts
# params.add_section('ratio')
# params.set('ratio', 'cs', '1,-1')
# params.set('ratio', 'bf', '1,-2,1')
# params.set('ratio', 'bx', '1,-1,-1,1')
# 
# with open('params.ini', 'w') as f:
#     params.write(f)

# -------------- underlying --------------
underlying_dict = dict()
# ---- DCE ----
underlying_dict.update({'DCE.A':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.M':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.Y':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.C':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.CS':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.P':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.I':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.J':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.JM':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.L':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.V':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.PP':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# underlying_dict.update({'DCE.JD':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# ---- CZCE ----
underlying_dict.update({'CZCE.CF':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.SR':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.MA':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.TA':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.RM':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.OI':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.ZC':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# ---- SHFE ----
underlying_dict.update({'SHFE.RB':{'year_start':['2012'], 'month_list':['01','05','10'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.HC':{'year_start':['2012'], 'month_list':['01','05','10'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.CU':{'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.AL':{'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.ZN':{'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.PB':{'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.NI':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.SN':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.RU':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.AU':{'year_start':['2010'], 'month_list':['06','12'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.AG':{'year_start':['2010'], 'month_list':['06','12'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.BU':{'year_start':['2010'], 'month_list':['03','06','09','12'], 'last_day_shift':['-30']}})
# ---- CFFEX ----
underlying_dict.update({'CFFEX.T':{'year_start':['2012'], 'month_list':['03','06','09','12'], 'last_day_shift':['30']}})

underlying = configparser.SafeConfigParser()

# underlying configuration
for key, value in underlying_dict.items():
    underlying.add_section(key)
    for k,v in value.items():
#         print(k,v)
        underlying.set(key, k, ','.join(v))

with open('underlying.ini', 'w') as f:
    underlying.write(f)
    
    
# -------------- Wind sector id --------------
underlying_sample_dict = dict()
# underlying_sample_dict.update({'DCE.I':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_sample_dict.update({'DCE.A':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# underlying_sample_dict.update({'DCE.M':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# underlying_sample_dict.update({'DCE.Y':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_sample_dict.update({'CZCE.CF':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# underlying_sample_dict.update({'CZCE.SR':{'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_sample_dict.update({'SHFE.RB':{'year_start':['2012'], 'month_list':['01','05','10'], 'last_day_shift':['-30']}})
# underlying_sample_dict.update({'SHFE.HC':{'year_start':['2012'], 'month_list':['01','05','10'], 'last_day_shift':['-30']}})
# underlying_sample_dict.update({'SHFE.CU':{'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
# underlying_sample_dict.update({'CFFEX.T':{'year_start':['2012'], 'month_list':['03','06','09','12'], 'last_day_shift':['30']}})

underlying_sample = configparser.SafeConfigParser()
# underlying_sample configuration
for key, value in underlying_sample_dict.items():
    underlying_sample.add_section(key)
    for k,v in value.items():
#         print(k,v)
        underlying_sample.set(key, k, ','.join(v))

with open('underlying_sample.ini', 'w') as f:
    underlying_sample.write(f)
    
       
