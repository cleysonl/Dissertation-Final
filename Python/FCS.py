import numpy as np
import pandas as pd
import math
# from Wellbeing import *
# from Health import *
# from Security import *
from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator.measures.similarity_t1 import jaccard

class FCS(object):
    
    def __init__(self,inputs, rules_inp, in_values, rules_out):
        self.inputs = inputs
        self.rules_inp = rules_inp
        self.in_values = in_values
        self.rules_out = rules_out
        self.red = .2
        self.orange = .4
        self.delta = .2
        self.blue = .8
    

    def combination_rules(self):
        CR_matrix =np.zeros((len(self.rules_inp),len(self.inputs)))
        for i in range(len(self.rules_inp)):
            for j in range(len(self.inputs)):
                CR_matrix[i][j] = float(self.in_values[self.rules_inp[self.inputs[j]].iloc[i]].iloc[j])

        return CR_matrix

    def defuzzification(self):
        print(self.combination_rules())
        num=0
        den=0
        total = 0
        output_dict={"Red":0.2,"Orange":0.5,"Blue":0.8}
        def_matrix = self.combination_rules()

        for i in range(len(self.rules_inp)):
            min_v=1
            for j in range(len(self.inputs)):
                if (def_matrix[i][j]<=min_v):
                    min_v = def_matrix[i][j]
            # print(min_v)
            num += min_v*output_dict[self.rules_out['Colors'].iloc[i]]
            den += min_v
        print(num)
        print(den)
        if den ==0:
            total=0
        else:
            total = num/den
        return total

    def color(self):
        max_color=0
        dict_colors={0:"Red",1:"Orange",2:"Blue"}            
        out_color = self.defuzzification()
        r = FuzzySet(Trapezoidal(0,0,self.red,self.orange))
        o = FuzzySet(Trapezoidal(self.red,self.orange,self.orange+self.delta,self.blue))
        b = FuzzySet(Trapezoidal(self.orange+self.delta,self.blue,1,1))
        mv_colors =[r.calculate_membership(out_color),
                    o.calculate_membership(out_color),
                    b.calculate_membership(out_color)]
        arg_max = np.argmax(mv_colors)
        max_color = dict_colors[arg_max]
        return max_color






    