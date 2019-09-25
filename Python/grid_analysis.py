import pandas as pd
import numpy as np

"""
Analysis for Wellbeing
"""


colors = ['Red','Orange','Blue']
data_wellbeing = pd.read_csv('grid_finalwb.csv')
print(len(data_wellbeing))
bad_results = pd.DataFrame(columns=['Visits','Mind Exercise','FamilyInt','Color MCGDM','Weight MCGDM','Color FCS','MV FCS'])
i=0
b_r=0
b_o=0
o_b=0
o_r = 0
r_b=0
r_o =0
list_dif = []
for row in range(len(data_wellbeing)):
    if(data_wellbeing['Color MCGDM'].iloc[row]!=data_wellbeing['Color FCS'].iloc[row]):
        i+=1
        bad_results.loc[len(bad_results)]=data_wellbeing.iloc[row]

bad_results.to_csv('bad_wb.csv')

data = pd.read_csv('bad_wb.csv')
for row in range(len(data)):  
    if(data['Color MCGDM'].iloc[row]=='Blue' and data['Color FCS'].iloc[row]=='Orange'):
        b_o+=1
    elif (data['Color MCGDM'].iloc[row]=='Blue' and data['Color FCS'].iloc[row]=='Red'):
        b_r+=1
    elif (data['Color MCGDM'].iloc[row]=='Orange' and data['Color FCS'].iloc[row]=='Blue'):
        o_b+=1
    elif (data['Color MCGDM'].iloc[row]=='Orange' and data['Color FCS'].iloc[row]=='Red'):
        o_r+=1
    elif (data['Color MCGDM'].iloc[row]=='Red' and data['Color FCS'].iloc[row]=='Orange'):
        r_o+=1
    else:
        r_b+=1 

print([b_o,b_r,o_b,o_r,r_b,r_o])


"""
Analysis for Health

"""


data_health = pd.read_csv('grid_finalhealth.csv')
print(len(data_health))
bad_results = pd.DataFrame(columns=['Medicine','Physical Exercise','Ext Temperature','Color MCGDM','Weight MCGDM','Color FCS','MV FCS'])
i=0
b_r=0
b_o=0
o_b=0
o_r = 0
r_b=0
r_o =0
list_dif = []
for row in range(len(data_health)):
    if(data_health['Color MCGDM'].iloc[row]!=data_health['Color FCS'].iloc[row]):
        i+=1
        bad_results.loc[len(bad_results)]=data_health.iloc[row]

bad_results.to_csv('bad_h.csv')



data = pd.read_csv('bad_h.csv')
for row in range(len(data)):  
    if(data['Color MCGDM'].iloc[row]=='Blue' and data['Color FCS'].iloc[row]=='Orange'):
        b_o+=1
    elif (data['Color MCGDM'].iloc[row]=='Blue' and data['Color FCS'].iloc[row]=='Red'):
        b_r+=1
    elif (data['Color MCGDM'].iloc[row]=='Orange' and data['Color FCS'].iloc[row]=='Blue'):
        o_b+=1
    elif (data['Color MCGDM'].iloc[row]=='Orange' and data['Color FCS'].iloc[row]=='Red'):
        o_r+=1
    elif (data['Color MCGDM'].iloc[row]=='Red' and data['Color FCS'].iloc[row]=='Orange'):
        r_o+=1
    else:
        r_b+=1 

print([b_o,b_r,o_b,o_r,r_b,r_o])
