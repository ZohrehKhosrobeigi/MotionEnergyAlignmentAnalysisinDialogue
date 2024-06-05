# Perform Chi-square test
from scipy.stats import chi2_contingency


class ChiSquaredTest ():
    def chiSquaredTest(self, df_cross_table,wf):

        chi2, p, dof, ex = chi2_contingency (df_cross_table)
        wf.write ("\nChi2: "+str(chi2)+"    p-value: " +str(p)+"    dof:    "+str(dof))

        if p < 0.05:
            wf.write ("\nSignificant result\n")
        else:
            wf.write ("\nNot significant\n")
