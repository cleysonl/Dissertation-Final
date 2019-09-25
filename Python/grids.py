from MCGDM import *
from Wellbeing import *
from Health import *
from Security import *
from FCS import *
import pandas as pd
import csv


#Wellbeing variables

inputs_wellbeing =['Visits','Mind Exercise','FamilyInt']
inputs_health =['Medicine','Physical Exercise','Ext Temperature']
inputs_security =['Location','Mobility','Environment']

rulesw = pd.read_excel('rules.xlsx', sheet_name='Wellbeing')
rulesh = pd.read_excel('rules.xlsx', sheet_name='Health')
ruless = pd.read_excel('rules.xlsx', sheet_name='Security')

rules_inpw = rulesw[['Visits','Mind Exercise','FamilyInt']]
rules_inph = rulesh[['Medicine','Physical Exercise','Ext Temperature']]
rules_inps = ruless[['Location','Mobility','Environment']]
rules_outw = rulesw[['Colors']]
rules_outh = rulesh[['Colors']]
rules_outs = ruless[['Colors']]


###### Grid  Wellbeing#####
n=0
grid_wellbeing = pd.DataFrame(columns=['Visits','Mind Exercise','FamilyInt','Color MCGDM','Weight MCGDM','Color FCS','MV FCS'])
for nvisits in range(0,30,2):
    for texercise in range(0,120,6):
        for temp in range(0,30,2):                
            in_values_wellbeing = {"num_visits": nvisits/30,"t_exercise": texercise/120,"ext_temp": temp/30}  
            in_valueswb = Wellbeing(in_values_wellbeing["num_visits"],
                                    in_values_wellbeing["t_exercise"],
                                    in_values_wellbeing["ext_temp"])
            wellbeingm= MCGDM(inputs_wellbeing, rules_inpw, in_valueswb.mv_wellbeing(), rules_outw)
            wellbeingf= FCS(inputs_wellbeing, rules_inpw, in_valueswb.mv_wellbeing(), rules_outw)
            grid_wellbeing.loc[len(grid_wellbeing)] = [nvisits,texercise, temp, wellbeingm.weight()[0],wellbeingm.weight()[1],wellbeingf.color(),wellbeingf.defuzzification()]
            n+=1
            print(n)
            # i+=1
grid_wellbeing.to_csv('grid_finalwb.csv')



###### Grid Health #####
n=0
grid_health= pd.DataFrame(columns=['Medicine','Physical Exercise','Ext Temperature','Color MCGDM','Weight MCGDM','Color FCS','MV FCS'])
for meds in range(0,100,5):
    print(meds)
    for pressure in range(0,120,6):
        print(pressure)
        for btemp in range(0,40,2):                
            in_values_health = {"med": meds/100,"press": pressure/120,"b_temp": btemp/50}  
            in_valuesh = Health(in_values_health["med"],
                                    in_values_health["press"],
                                    in_values_health["b_temp"])
            healthm= MCGDM(inputs_health, rules_inph, in_valuesh.mv_health(), rules_outh)
            healthf= FCS(inputs_health, rules_inph, in_valuesh.mv_health(), rules_outh)
            grid_health.loc[len(grid_health)] = [meds,pressure, btemp, healthm.weight()[0],healthm.weight()[1],healthf.color(),healthf.defuzzification()]
            n+=1
            print(n)
            # i+=1
grid_health.to_csv('grid_finalhealth.csv')













           