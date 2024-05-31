#THIS CODE COMPUTES THE SPEARMAN CORRELATION OF TWO SERIES.
#IF IT CANNOT COMPUTE FOR ANY REASON PRINT THE X AND Y
#IF THE LENGHT OF X AND Y IS NOT EQUAL IT RETURES 1000

from scipy.stats import spearmanr
from statistics import stdev
import math

class SpearmanComputation ():
    def __init__(self):
        self.spear, self.pValue,self.fisherz= 0, 1,0

    def scipyLibCorrealtion(self,x, y,wf):

        x = x.astype ('float64')
        y = y.astype ('float64')
        try:
            #print("this is x:   ",x,"this is y   ", y)
            #handle if their lengh is not equvalent

            if len (x)==len(y):
                self.spear, self.pValue = spearmanr (x, y, nan_policy='omit')
                #self.fisherz=fisher_z(self.spear)


                return self.spear, self.pValue,self.fisherz
            else:
                wf.write ("\nError Computing CC is x is" + str (x)+" Y is"+"\n")
                return 10000,10000,10000
        except Exception as e:
            wf.write ("\nError CC: " + e +" x is" + str (x)+" Y is"+"\n")

            return 10000, 10000



