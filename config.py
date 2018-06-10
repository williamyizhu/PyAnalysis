import os
import configparser
# os.chdir('Z:\Documents\workspace\PyAnalysis')
print(os.getcwd())

# -------------- month --------------
A010509 = ';'.join([str(i).zfill(2) for i in [1,5,9]])
B010509 = ';'.join([str(i).zfill(2) for i in [5,9]] + [str(i).zfill(2)+'+1' for i in [1]])
C010509 = ';'.join([str(i).zfill(2) for i in [9]]   + [str(i).zfill(2)+'+1' for i in [1,5]])

A010510 = ';'.join([str(i).zfill(2) for i in [1,5,10]])
B010510 = ';'.join([str(i).zfill(2) for i in [5,10]] + [str(i).zfill(2)+'+1' for i in [1]])
C010510 = ';'.join([str(i).zfill(2) for i in [10]]   + [str(i).zfill(2)+'+1' for i in [1,5]])

A12 = ';'.join([str(i).zfill(2) for i in list(range(1,13))])
B12 = ';'.join([str(i).zfill(2) for i in list(range(2,13))] + [str(i).zfill(2)+'+1' for i in list(range(1,2))])
C12 = ';'.join([str(i).zfill(2) for i in list(range(3,13))] + [str(i).zfill(2)+'+1' for i in list(range(1,3))])

A0612 = ';'.join([str(i).zfill(2) for i in [6,12]])
B0612 = ';'.join([str(i).zfill(2) for i in [12]] + [str(i).zfill(2)+'+1' for i in [6]])
C0612 = ';'.join([str(i).zfill(2) for i in []]   + [str(i).zfill(2)+'+1' for i in [6,12]])

A03060912 = ';'.join([str(i).zfill(2) for i in [3,6,9,12]])
B03060912 = ';'.join([str(i).zfill(2) for i in [6,9,12]] + [str(i).zfill(2)+'+1' for i in [3]])
C03060912 = ';'.join([str(i).zfill(2) for i in [9,12]]   + [str(i).zfill(2)+'+1' for i in [3,6]])

# -------------- calendar --------------
calendar_dict = dict()
# ---- DCE ----
calendar_dict.update({'DCE.A_CS':{'asset_class':['ARGS'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.M_CS':{'asset_class':['ARGS'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.Y_CS':{'asset_class':['ARGS'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.C_CS':{'asset_class':['ARGS'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.CS_CS':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.P_CS':{'asset_class':['ARGS'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.JD_CS':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.I_CS':{'asset_class':['FERR'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.J_CS':{'asset_class':['FERR'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.JM_CS':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.L_CS':{'asset_class':['CHEM'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.V_CS':{'asset_class':['CHEM'],  'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'DCE.PP_CS':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
# ---- CZCE ----
calendar_dict.update({'CZCE.CF_CS':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'CZCE.SR_CS':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'CZCE.RM_CS':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'CZCE.OI_CS':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'CZCE.MA_CS':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'CZCE.TA_CS':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'CZCE.ZC_CS':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
# ---- SHFE ----
calendar_dict.update({'SHFE.CU_CS':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.AL_CS':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.ZN_CS':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.PB_CS':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.NI_CS':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.SN_CS':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.RB_CS':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010510,B010510], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.HC_CS':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010510,B010510], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.RU_CS':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.BU_CS':{'asset_class':['CHEM'], 'year':['2010','2020'], 'month':[A03060912,B03060912], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.AU_CS':{'asset_class':['PMET'], 'year':['2010','2020'], 'month':[A0612,B0612], 'last_day_shift':['0']}})
calendar_dict.update({'SHFE.AG_CS':{'asset_class':['PMET'], 'year':['2010','2020'], 'month':[A0612,B0612], 'last_day_shift':['0']}})
# ---- CFFEX ----
calendar_dict.update({'CFFEX.T_CS':{'asset_class':['TREA'], 'year':['2012','2020'], 'month':[A03060912,B03060912], 'last_day_shift':['0']}})

# calendar configuration
calendar = configparser.SafeConfigParser()
for key, value in calendar_dict.items():
    value['exul'] = [key.split('_')[0]] * 2
    value['combo_type'] = [key.split('_')[1]]
    value['ratio'] = ['1','-1']
    calendar.add_section(key)
    for k,v in value.items():
#         print(k,v)
        calendar.set(key, k, ','.join(v))

with open('calendar.ini', 'w') as f:
    calendar.write(f)

# -------------- butterfly --------------
butterfly_dict = dict()
# ---- DCE ----
butterfly_dict.update({'DCE.A_BF' :{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.M_BF' :{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.Y_BF' :{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.C_BF' :{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.CS_BF':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.P_BF' :{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.JD_BF':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.I_BF' :{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.J_BF' :{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.JM_BF':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.L_BF' :{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.V_BF' :{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'DCE.PP_BF':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
# ---- CZCE ----
butterfly_dict.update({'CZCE.CF_BF':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'CZCE.SR_BF':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'CZCE.RM_BF':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'CZCE.OI_BF':{'asset_class':['ARGS'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'CZCE.MA_BF':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'CZCE.TA_BF':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'CZCE.ZC_BF':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
# ---- SHFE ----
butterfly_dict.update({'SHFE.CU_BF':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12,C12], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.AL_BF':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12,C12], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.ZN_BF':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12,C12], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.PB_BF':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A12,B12,C12], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.NI_BF':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.SN_BF':{'asset_class':['BMET'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.RB_BF':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010510,B010510,C010510], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.HC_BF':{'asset_class':['FERR'], 'year':['2012','2020'], 'month':[A010510,B010510,C010510], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.RU_BF':{'asset_class':['CHEM'], 'year':['2012','2020'], 'month':[A010509,B010509,C010509], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.BU_BF':{'asset_class':['CHEM'], 'year':['2010','2020'], 'month':[A03060912,B03060912,C03060912], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.AU_BF':{'asset_class':['PMET'], 'year':['2010','2020'], 'month':[A0612,B0612,C0612], 'last_day_shift':['0']}})
butterfly_dict.update({'SHFE.AG_BF':{'asset_class':['PMET'], 'year':['2010','2020'], 'month':[A0612,B0612,C0612], 'last_day_shift':['0']}})
# ---- CFFEX ----
butterfly_dict.update({'CFFEX.T_BF':{'asset_class':['TREA'], 'year':['2012','2020'], 'month':[A03060912,B03060912,C03060912], 'last_day_shift':['0']}})

# butterfly configuration
butterfly = configparser.SafeConfigParser()
for key, value in butterfly_dict.items():
    value['exul'] = [key.split('_')[0]] * 3
    value['combo_type'] = [key.split('_')[1]]
    value['ratio'] = ['1','-2','1']
    butterfly.add_section(key)
    for k,v in value.items():
#         print(k,v)
        butterfly.set(key, k, ','.join(v))

with open('butterfly.ini', 'w') as f:
    butterfly.write(f)

# -------------- combo --------------
combo_dict = dict()

# ------- ICS -------
combo_dict.update({'SHFE.RB_SHFE.HC_ICS':{'asset_class':['FERR'], 'exul':['SHFE.RB','SHFE.HC'], 'year':['2010','2020'], 'month':[A010510,A010510], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.J_DCE.JM_ICS'   :{'asset_class':['FERR'], 'exul':['DCE.J','DCE.JM'],    'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})

combo_dict.update({'DCE.M_CZCE.RM_ICS'  :{'asset_class':['ARGS'], 'exul':['DCE.M','CZCE.RM'],   'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.Y_CZCE.OI_ICS'  :{'asset_class':['ARGS'], 'exul':['DCE.Y','CZCE.OI'],   'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.Y_DCE.P_ICS'    :{'asset_class':['ARGS'], 'exul':['DCE.Y','DCE.P'],     'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.A_DCE.B_ICS'    :{'asset_class':['ARGS'], 'exul':['DCE.A','DCE.B'],     'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})

combo_dict.update({'DCE.L_DCE.V_ICS'    :{'asset_class':['CHEM'], 'exul':['DCE.L','DCE.V'],     'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.L_DCE.PP_ICS'   :{'asset_class':['CHEM'], 'exul':['DCE.L','DCE.PP'],    'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.PP_CZCE.MA_ICS' :{'asset_class':['CHEM'], 'exul':['DCE.PP','CZCE.MA'],  'year':['2010','2020'], 'month':[A010509,A010509], 'combo_type':['COMBO'], 'ratio':['1','-3'], 'last_day_shift':['0']}})

# ------- BX -------
combo_dict.update({'SHFE.RB_SHFE.HC_BX' :{'asset_class':['FERR'], 'exul':['SHFE.RB','SHFE.RB','SHFE.HC','SHFE.HC'], 'year':['2010','2020'], 'month':[A010510,B010510,A010510,B010510], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.J_DCE.JM_BX'    :{'asset_class':['FERR'], 'exul':['DCE.J','DCE.J','DCE.JM','DCE.JM'],       'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})

combo_dict.update({'DCE.M_CZCE.RM_BX'   :{'asset_class':['ARGS'], 'exul':['DCE.M','DCE.M','CZCE.RM','CZCE.RM'],     'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.Y_CZCE.OI_BX'   :{'asset_class':['ARGS'], 'exul':['DCE.Y','DCE.Y','CZCE.OI','CZCE.OI'],     'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.Y_DCE.P_BX'     :{'asset_class':['ARGS'], 'exul':['DCE.Y','DCE.Y','DCE.P','DCE.P'],         'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.A_DCE.B_BX'     :{'asset_class':['ARGS'], 'exul':['DCE.A','DCE.A','DCE.B','DCE.B'],         'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})

combo_dict.update({'DCE.L_DCE.V_BX'     :{'asset_class':['CHEM'], 'exul':['DCE.L','DCE.L','DCE.V','DCE.V'],         'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.L_DCE.PP_BX'    :{'asset_class':['CHEM'], 'exul':['DCE.L','DCE.L','DCE.PP','DCE.PP'],       'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-1','1'], 'last_day_shift':['0']}})
combo_dict.update({'DCE.PP_CZCE.MA_BX'  :{'asset_class':['CHEM'], 'exul':['DCE.PP','DCE.PP','CZCE.MA','CZCE.MA'],   'year':['2010','2020'], 'month':[A010509,B010509,A010509,B010509], 'combo_type':['COMBO'], 'ratio':['1','-1','-3','3'], 'last_day_shift':['0']}})

# ------- Others -------
combo_dict.update({'STEELMILL'          :{'asset_class':['FERR'], 'exul':['DCE.I','DCE.J','SHFE.RB'],               'year':['2010','2020'], 'month':[A010509,A010509,A010510],         'combo_type':['COMBO'], 'ratio':['-2','-1','1'],      'last_day_shift':['0']}})
combo_dict.update({'CRUSH'              :{'asset_class':['ARGS'], 'exul':['DCE.A','DCE.M','SHFE.Y'],                'year':['2010','2020'], 'month':[A010509,A010509,A010509],         'combo_type':['COMBO'], 'ratio':['-5','4','1'],       'last_day_shift':['0']}})

# combo configuration
combo = configparser.SafeConfigParser()
for key, value in combo_dict.items():
    combo.add_section(key)
    for k,v in value.items():
#         print(k,v)
        combo.set(key, k, ','.join(v))

with open('combo.ini', 'w') as f:
    combo.write(f)
