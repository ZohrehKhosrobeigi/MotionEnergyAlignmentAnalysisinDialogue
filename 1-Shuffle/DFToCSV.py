import os
import pandas as pd

class DfToCSV():
    def dfToCSV(self,dataframe,filename):

        column_names = list (dataframe.columns.values)

              # Check if the CSV fmotion already exists
        if os.path.exists(filename):
            # Append the DataFrame without the header_generated
            dataframe.to_csv(filename, mode='a', header=False, index=False,sep=',', encoding='utf-8', columns=column_names)
        else:
            # Write the DataFrame with the header_generated
            dataframe.to_csv(filename, index=False,sep=',', encoding='utf-8', columns=column_names)

