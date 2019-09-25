import numpy as np
import pandas as pd
from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator import global_settings as gs


# gs.global_uod = (0, 120)


class Wellbeing(object):

    def __init__(self,num_visits,t_exercise,ext_temp):
        self.num_visits = num_visits
        self.t_exercise = t_exercise
        self.ext_temp = ext_temp
    
    def visits(self):
        """ MF for pyhsical visits from family members or friends per week"""
        gs.global_uod = (0, 1)
        mv_visits = []

        low_v = FuzzySet(Trapezoidal(0,0,2/30,5/30))
        med_v = FuzzySet(Trapezoidal(3/30,7/30,7/30,14/30))
        high_v = FuzzySet(Trapezoidal(7/30,14/30,30/30,30/30))

        mv_visits = [low_v.calculate_membership(self.num_visits),
                     med_v.calculate_membership(self.num_visits),
                     high_v.calculate_membership(self.num_visits)]

        return mv_visits

    def exercise(self):
        """ MF for daily time using mind games per week"""
        gs.global_uod = (0, 1)
        mv_exercise = []

        low_ex = FuzzySet(Trapezoidal(0,0,15/120,20/120))
        med_ex = FuzzySet(Trapezoidal(15/120,15/120,30/120,60/120))
        high_ex = FuzzySet(Trapezoidal(30/120,60/120,120/120,120/120))

        mv_exercise = [low_ex.calculate_membership(self.t_exercise),
                       med_ex.calculate_membership(self.t_exercise),
                       high_ex.calculate_membership(self.t_exercise)]
        return mv_exercise

    def temperature(self):
        """ MF for family interactions via the device and SM per week"""
        gs.global_uod = (0, 1)
        
        mv_temp = []
        
        low_temp = FuzzySet(Trapezoidal(0,0,2/30,5/30))
        med_temp = FuzzySet(Trapezoidal(3/30,7/30,7/30,14/30))
        high_temp = FuzzySet(Trapezoidal(7/30,14/30,30/30,30/30))

        mv_temp = [low_temp.calculate_membership(self.ext_temp),
                       med_temp.calculate_membership(self.ext_temp),
                       high_temp.calculate_membership(self.ext_temp)]
        return mv_temp

    def mv_wellbeing(self):
        table_wellbeing = pd.DataFrame([self.visits(),self.exercise(),self.temperature()], columns=["Low","Med","High"])
        return table_wellbeing
