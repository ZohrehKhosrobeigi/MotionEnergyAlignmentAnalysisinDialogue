import pandas as pd
class CSVDFReader():

    def csvdfReader(self,inputfile):
        self.df_motion = pd.read_csv (inputfile)
        print(f'{inputfile} is read and added successfully')
        return self.df_motion
