import numpy as np
import pandas as pd
from datetime import datetime

from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator import global_settings as gs


# gs.global_uod = (0, 1)


class Health(object):

    def __init__(self,med,p_exercise,temp):
        self.med = med
        self.p_exercise = p_exercise
        self.temp = temp
    
    def medicine(self):
        """ MF for: % of times the patient has taken its medicine"""
        gs.global_uod = (0, 1)
        mv_medicine = []

        low_m = FuzzySet(Trapezoidal(0,0,.2,.3))
        med_m = FuzzySet(Trapezoidal(.2,.3,.5,.6))
        high_m = FuzzySet(Trapezoidal(.5,.6,1,1))

        mv_medicine = [low_m.calculate_membership(self.med),
                       med_m.calculate_membership(self.med),
                       high_m.calculate_membership(self.med)]

        return mv_medicine

    def phys_exercise(self):
        """ MF for the physical exercise of the patient"""
        gs.global_uod = (0, 1)

        mv_p_exercise = []    

        low_p_exercise = FuzzySet(Trapezoidal(0,0,15/120,20/120))
        med_p_exercise = FuzzySet(Trapezoidal(15/120,15/120,30/120,60/120))
        high_p_exercise = FuzzySet(Trapezoidal(30/120,60/120,120/120,120/120))

        mv_p_exercise = [low_p_exercise.calculate_membership(self.p_exercise),
                       med_p_exercise.calculate_membership(self.p_exercise),
                       high_p_exercise.calculate_membership(self.p_exercise)]

        return mv_p_exercise

    def ext_temp(self):
        """ MF for the exteriors temperature"""
        gs.global_uod = (0, 1)
        mv_temp = []
        
        low_temp = FuzzySet(Trapezoidal(0,0,10/50,20/50))
        med_temp = FuzzySet(Trapezoidal(10/50,20/50,25/50,30/50))
        high_temp = FuzzySet(Trapezoidal(20/50,30/50,50/50,50/50))

        mv_temp = [low_temp.calculate_membership(self.temp),
                       med_temp.calculate_membership(self.temp),
                       high_temp.calculate_membership(self.temp)]

        return mv_temp

    def mv_health(self):
        table_health = pd.DataFrame([self.medicine(),self.phys_exercise(),self.ext_temp()], columns=["Low","Med","High"])
        return table_health
