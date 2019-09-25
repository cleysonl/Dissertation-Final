"""
     Steps:
        1) Get the data from the Experts (file)
        2) Use MFs (Use fuzzycreator library to generate the sets)
        3) Get inputs to calculate the MF and the output with respect to the IAA generated Fuzzy Set's  (Use fuzzycreator to obtain the MFs values for the inputs)
        4) Use MCGDM to get the output and take a decision (CLGDM)
            1) Decision matrices and reciprocal decision matrices (for each possible output)
            2) Calculate the cumulative decision matrices
            3) Calculate the average cumulative matrices
            4) Normalization of ACM
            5) Calculation of weights
"""

from MCGDM import *
from Wellbeing import *
from Health import *
from Security import *
from FCS import *
import pandas as pd
from fuzzycreator.measures.similarity_t1 import jaccard

# Variables

inputs_wellbeing =['Visits','Mind Exercise','FamilyInt']
inputs_health =['Medicine','Physical Exercise','Ext Temperature']
inputs_security =['Location','Mobility','Environment']

# Remove comment # for aspect analyzed (Wellbeing or Health)
# in_values_wellbeing = {"num_visits": 14,"t_exercise": 30,"ext_temp": 25}  #BLUE
in_values_wellbeing = {"num_visits": 7.05/30 ,"t_exercise": 0.5,"ext_temp": 13.2/30}  
# in_values_health = {"med": 0.91,"press": 0.102,"b_temp": 0.657}
# in_values_security = {"loc": 0.5,"mob": 3,"env": 2.5}

# Reads the rules from an excel file
rulesw = pd.read_excel('rules.xlsx', sheet_name='Wellbeing')
rulesh = pd.read_excel('rules.xlsx', sheet_name='Health')
ruless = pd.read_excel('rules.xlsx', sheet_name='Security')

# Ways to separate outputs and inputs from the rules database

rules_inpw = rulesw[['Visits','Mind Exercise','FamilyInt']]
rules_inph = rulesh[['Medicine','Physical Exercise','Ext Temperature']]
rules_inps = ruless[['Location','Mobility','Environment']]
rules_outw = rulesw[['Colors']]
rules_outh = rulesh[['Colors']]
rules_outs = ruless[['Colors']]


# Remove comments depending on which aspect wants to be evaluated
## Wellbeing
in_valueswb = Wellbeing(in_values_wellbeing["num_visits"],
              in_values_wellbeing["t_exercise"],
              in_values_wellbeing["ext_temp"])
print(in_valueswb.mv_wellbeing())

## Health
# in_valuesh = Health(in_values_health["med"],
#               in_values_health["press"],
#               in_values_health["b_temp"])
# print(in_valuesh.mv_health())

## Security
# in_valuess = Security(in_values_security["loc"],
#               in_values_security["mob"],
#             in_values_security["env"])
# print(in_valuess.mv_security())

## For each aspect the MCGDM and FCS classes are called below

### Wellbeing ####
# wellbeing= MCGDM(inputs_wellbeing, rules_inpw, in_valueswb.mv_wellbeing(), rules_outw)
# print(wellbeing.weight()[0])
# print(wellbeing.weight()[1])
wellbeing= FCS(inputs_wellbeing, rules_inpw, in_valueswb.mv_wellbeing(), rules_outw)
print(wellbeing.defuzzification())
print(wellbeing.color())

## Health ###
# health= MCGDM(inputs_health, rules_inph, in_valuesh.mv_health(), rules_outh)
# print(health.weight()[0])
# print(health.weight()[1])
# health= FCS(inputs_health, rules_inph, in_valuesh.mv_health(), rules_outh)
# print(health.defuzzification())
# print(health.color())

## Security ###
# security= MCGDM(inputs_security, rules_inps, in_valuess.mv_security(), rules_outs)
# print(security.weight()[0])
# print(security.weight()[1])
# security= FCS(inputs_security, rules_inps, in_valuess.mv_security(), rules_outs)
# print(security.defuzzification())
# print(security.color())


