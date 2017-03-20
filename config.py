import os
import configparser

# os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyAnalysis')
print(os.getcwd())

# -------------- underlying --------------
underlying_dict = dict()
# ---- DCE ----
underlying_dict.update({'DCE.A':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.M':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.Y':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.C':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.CS':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.P':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# underlying_dict.update({'DCE.JD':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.I':{'asset_class':['FERR'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.J':{'asset_class':['FERR'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.JM':{'asset_class':['FERR'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.L':{'asset_class':['CHEM'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.V':{'asset_class':['CHEM'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'DCE.PP':{'asset_class':['CHEM'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# ---- CZCE ----
underlying_dict.update({'CZCE.CF':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.SR':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.RM':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.OI':{'asset_class':['ARGS'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.MA':{'asset_class':['CHEM'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.TA':{'asset_class':['CHEM'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'CZCE.ZC':{'asset_class':['FERR'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
# ---- SHFE ----
underlying_dict.update({'SHFE.RB':{'asset_class':['FERR'], 'year_start':['2012'], 'month_list':['01','05','10'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.HC':{'asset_class':['FERR'], 'year_start':['2012'], 'month_list':['01','05','10'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.CU':{'asset_class':['BMET'], 'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.AL':{'asset_class':['BMET'], 'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.ZN':{'asset_class':['BMET'], 'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.PB':{'asset_class':['BMET'], 'year_start':['2015'], 'month_list':[str(i).zfill(2) for i in list(range(1,13))], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.NI':{'asset_class':['BMET'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.SN':{'asset_class':['BMET'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.RU':{'asset_class':['CHEM'], 'year_start':['2012'], 'month_list':['01','05','09'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.BU':{'asset_class':['CHEM'], 'year_start':['2010'], 'month_list':['03','06','09','12'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.AU':{'asset_class':['PMET'], 'year_start':['2010'], 'month_list':['06','12'], 'last_day_shift':['-30']}})
underlying_dict.update({'SHFE.AG':{'asset_class':['PMET'], 'year_start':['2010'], 'month_list':['06','12'], 'last_day_shift':['-30']}})
# ---- CFFEX ----
underlying_dict.update({'CFFEX.T':{'asset_class':['INTR'], 'year_start':['2012'], 'month_list':['03','06','09','12'], 'last_day_shift':['30']}})

underlying = configparser.SafeConfigParser()

# underlying configuration
for key, value in underlying_dict.items():
    underlying.add_section(key)
    for k,v in value.items():
#         print(k,v)
        underlying.set(key, k, ','.join(v))

with open('underlying.ini', 'w') as f:
    underlying.write(f)
