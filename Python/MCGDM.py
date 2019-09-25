import numpy as np
from math import exp

class MCGDM(object):

    def __init__(self, inputs, rules_inp, in_values, rules_out):
        """ This class MCGDM """
        self.inputs = inputs
        self.rules_inp = rules_inp
        self.in_values = in_values
        self.rules_out = rules_out

    def decision_matrix(self,n_inp):
        R_matrix =np.zeros((len(self.inputs),len(self.inputs)))

        for i in range(len(self.inputs)):
            for j in range(len(self.inputs)):
                if i==j:
                    ## Evaluate the sigmoid depending on rule and input
                    R_matrix[i][j]+=0.5
                elif j>i:
                    R_matrix[i][j]+= min(float(self.in_values[self.rules_inp.iloc[n_inp][i]].iloc[i]),

                                         float(self.in_values[self.rules_inp.iloc[n_inp][j]].iloc[j]))                   
                else:
                    R_matrix[i][j]+= 1 - R_matrix[j][i]
        return R_matrix

    def cumulative_matrix(self):

        #Remove duplicate and create a list of the different outputs
        output_set = list(set(self.rules_out['Colors']))
    
        #Create the list to save the cumulative matrices
        list_cm = []
        # Loop to create for every different output their cumulative matrices
        for output in output_set:
            # print(output)
            cum_matrix =np.zeros((len(self.inputs),len(self.inputs)))
            counter = 0
            n_inp = 0
            # print(output)
            for rule in range(len(self.rules_out)):
                if self.rules_out['Colors'].iloc[rule]==output:
                    print("Decision Matrix: {}".format(n_inp))
                    print(self.decision_matrix(n_inp) )
                    cum_matrix += self.decision_matrix(n_inp) 
                    counter+=1    
                # Keeps record of the number of rule we are checking to call the righ one for te function decision_matrix inside the if
                n_inp +=1      
            list_cm.append((output,cum_matrix/counter))
        print("List Cum Matrices:")
        print(list_cm)
        return list_cm

    def acumulative_matrices(self):
        # Average cumulative matrices:
        list_acm = []
        for matrix in self.cumulative_matrix():
            acm = np.zeros(len(self.inputs))
            for i in range(len(self.inputs)):
                for j in range(len(self.inputs)):
                    acm[i]+=matrix[1][i][j]
            list_acm.append((matrix[0],acm/len(self.inputs)))
        print("List ACum Matrices:")
        print(list_acm)
        return list_acm


    #Normalization
    def normalization(self):
        #Remove duplicate and create a list of the different outputs
        output_set = list(set(self.rules_out['Colors']))

        #List where the normalized ACM are saved
        list_norm =[]
        list_acum = self.acumulative_matrices()
        for n in range(len(output_set)):
            norm_vec = np.zeros(len(output_set))
            for i in range(len(output_set)):
                d=0
                for j in range(len(output_set)):
                    d = d +  list_acum[j][1][n]
                norm_vec[i] = list_acum[i][1][n]/d
            list_norm.append(norm_vec)
        print("List Normalization Matrices:")
        print(list_norm)    
        return list_norm

    #Weights
    def weight(self):
        #Remove duplicate and create a list of the different outputs
        output_set = list(set(self.rules_out['Colors']))

        weights =[]
        for n in range(len(self.inputs)):
            w=0
            for i in self.normalization():
                w += i[n]
            weights.append(w/len(self.inputs))
        print("Weights:")
        print(weights)
        # Check the largest weight and choose the output corresponding to that weight
        alpha=0
        i=0
        r =0
        for w in weights:
            if w> alpha:
                alpha = w
                r=i
            i+=1
        return (output_set[r],alpha)

    def printer(self):
        result = self.weight()
        print(result)
