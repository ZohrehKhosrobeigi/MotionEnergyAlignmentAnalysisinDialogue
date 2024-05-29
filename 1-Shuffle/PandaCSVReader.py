import pandas as pd
import numpy as np

class PandaCSVReader():
    def pandaCSVReader(self,filename):

        # making df2_in2 frame

        self.df_data = pd.read_csv (filename)
        #print(f"The shape of ",filename_png,"is         ",self.df_data.shape[0])
        return self.df_data