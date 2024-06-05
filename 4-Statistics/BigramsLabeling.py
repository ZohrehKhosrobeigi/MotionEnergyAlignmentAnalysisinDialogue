# labeling bigrams of windows
import numpy as np
import pandas as pd

class BigramsLabeling():
    # this method defines bigrams of data and return cross tables of lables of to different data
    def bigrmasLabeling(self,df_actual,df_manipulated,threshold,session):
        df_actual['L0SigBin'] = np.where (df_actual['Pval_Lag_0_second'] < threshold, 1, 0)
        df_actual['L0SigC'] = np.where (df_actual['Pval_Lag_0_second'] < threshold,
                                        np.where (df_actual['Coeff_Lag_0_second'] < 0, "Neg", "Pos"), "Open")

        df_manipulated['L0SigBin'] = np.where (df_manipulated['Pval_Lag_0_second'] < threshold, 1, 0)
        df_manipulated['L0SigC'] = np.where (df_manipulated['Pval_Lag_0_second'] < threshold,
                                          np.where (df_manipulated['Coeff_Lag_0_second'] < 0, "Neg", "Pos"), "Open")

        # Process Da for the current session
        session_d1 = df_actual[df_actual['Session'] == session]
        time_series_d1 = session_d1['L0SigC'].values
        three_grams_d1 = [f"{time_series_d1[i]} {time_series_d1[i + 1]}" for i in range (len (time_series_d1) - 1)]
        Da3grams_d1 = pd.DataFrame ({'ngrams': three_grams_d1, 'Resource': 'DActual'})

        # Process Dr for the current session
        session_d2 = df_manipulated[df_manipulated['Session'] == session]
        time_series_d2 = session_d2['L0SigC'].values
        three_grams_d2 = [f"{time_series_d2[i]} {time_series_d2[i + 1]}" for i in range (len (time_series_d2) - 1)]
        Dr3grams_d2 = pd.DataFrame ({'ngrams': three_grams_d2, 'Resource': 'DManipulated'})

        # Combine and create cross-tabulation
        Dallgrams = pd.concat ([Da3grams_d1, Dr3grams_d2], ignore_index=True)
        self.df_all_grams=Dallgrams
        return self.df_all_grams

