import numpy as np
import pandas as pd
from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator import global_settings as gs


# gs.global_uod = (0, 120)


class Wellbeing(object):

    def __init__(self, num_visits, m_exercise, familyint):
        self.num_visits = num_visits
        self.m_exercise = m_exercise
        self.familyint = familyint
    
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

        mv_visits =[float(i) for i in mv_visits]

        return mv_visits

    def mind_exercise(self):
        """ MF for daily time using mind games per week"""
        gs.global_uod = (0, 1)
        mv_mind_exercise = []

        low_m_ex = FuzzySet(Trapezoidal(0,0,15/120,20/120))
        med_m_ex = FuzzySet(Trapezoidal(15/120,15/120,30/120,60/120))
        high_m_ex = FuzzySet(Trapezoidal(30/120,60/120,120/120,120/120))

        mv_mind_exercise = [low_m_ex.calculate_membership(self.m_exercise),
                            med_m_ex.calculate_membership(self.m_exercise),
                            high_m_ex.calculate_membership(self.m_exercise)]

        mv_mind_exercise = [float(i) for i in mv_mind_exercise]   

        return mv_mind_exercise

    def family_int(self):
        """ MF for family interactions via the device and SM per week"""
        gs.global_uod = (0, 1)
        
        mv_fam_int = []
        
        low_fam_int = FuzzySet(Trapezoidal(0,0,2/30,5/30))
        med_fam_int = FuzzySet(Trapezoidal(3/30,7/30,7/30,14/30))
        high_fam_int = FuzzySet(Trapezoidal(7/30,14/30,30/30,30/30))

        mv_fam_int = [low_fam_int.calculate_membership(self.familyint),
                       med_fam_int.calculate_membership(self.familyint),
                       high_fam_int.calculate_membership(self.familyint)]
        
        mv_fam_int = [float(i) for i in mv_fam_int]

        return mv_fam_int

    def mv_wellbeing(self):
        table_wellbeing = pd.DataFrame([self.visits(), self.mind_exercise(), self.family_int()], columns=["Low","Med","High"])
        return table_wellbeing
