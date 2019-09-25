import numpy as np
import pandas as pd
from datetime import datetime

from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator import global_settings as gs


# gs.global_uod = (0, 1)


class Health(object):

    def __init__(self,med,press,b_temp):
        self.med = med
        self.press = press
        self.b_temp = b_temp
    
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

    def pressure(self):
        """ MF for the physical exercise of the patient"""
        gs.global_uod = (0, 1)

        mv_pressure = []    

        low_p = FuzzySet(Trapezoidal(0,0,15/120,20/120))
        med_p = FuzzySet(Trapezoidal(15/120,15/120,30/120,60/120))
        high_p = FuzzySet(Trapezoidal(30/120,60/120,120/120,120/120))

        mv_pressure = [low_p.calculate_membership(self.press),
                       med_p.calculate_membership(self.press),
                       high_p.calculate_membership(self.press)]

        return mv_pressure

    def body_temp(self):
        """ MF for the exteriors temperature"""
        gs.global_uod = (0, 1)
        mv_body_temp = []
        
        low_btemp = FuzzySet(Trapezoidal(0,0,10/50,20/50))
        med_btemp = FuzzySet(Trapezoidal(10/50,20/50,25/50,30/50))
        high_btemp = FuzzySet(Trapezoidal(20/50,30/50,50/50,50/50))

        mv_body_temp = [low_btemp.calculate_membership(self.b_temp),
                       med_btemp.calculate_membership(self.b_temp),
                       high_btemp.calculate_membership(self.b_temp)]

        return mv_body_temp

    def mv_health(self):
        table_health = pd.DataFrame([self.medicine(),self.pressure(),self.body_temp()], columns=["Low","Med","High"])
        return table_health
