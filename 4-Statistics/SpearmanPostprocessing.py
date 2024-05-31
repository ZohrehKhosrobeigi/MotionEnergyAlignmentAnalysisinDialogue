#THIS CLASS HANDLE OUTPUT OF SPEARMAN COMPUTATION CLASS, WRITE THE RESULTS IN TEXT FILS OR CONVERT NAN TO CC
import SpearmanComputation
import math
class SpearmanProcessor():
    def __init__(self):
        self.spear_coef=0
        self.pvalue_coef=1

    def spearmanProcess(self,motion_segment_pleft, motion_segment_pright,wf):


        # compute spearman and p value
        spear_comp = SpearmanComputation.SpearmanComputation ()
        self.spear_coef, self.pvalue_coef,_ = spear_comp.scipyLibCorrealtion (motion_segment_pleft,
                                                                                            motion_segment_pright,wf)  # the warning message are for when x has value but y has zero value
        ################################################################################################
        if self.spear_coef == 10000 and self.pvalue_coef == 10000:  # it happens when the onset and offset of window is larger than the number of frames
            self.spear_coef, self.pvalue_coef,self.fisherz= 0, 1,0
            wf.write ("\nError RRR: onset and offset of window is larger than the number of frames "  "\n")

        # to convert nan cc
        elif self.spear_coef != self.spear_coef or self.pvalue_coef != self.pvalue_coef :
            wf.write ("Warning: coefficient is nan, motion_segment_pleft is: "+str(motion_segment_pleft) +" motion_segment_pright is: "+str(motion_segment_pright) +"\n")
            self.spear_coef = 0
            self.pvalue_coef = 1
            self.fisherz=0

        else:# if i want to keep cc with sig pval, i must uncomment# self.spear_coef = 0 other wise this codition return all cc and all pvalues

            if self.pvalue_coef>0.05:
                # self.spear_coef = 0
                self.spear_coef = self.spear_coef
                self.pvalue_coef = self.pvalue_coef

            elif self.pvalue_coef <=0.05:
                self.spear_coef = self.spear_coef
                self.pvalue_coef = self.pvalue_coef

        return self.spear_coef, self.pvalue_coef