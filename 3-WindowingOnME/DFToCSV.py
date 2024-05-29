import os
class DfToCSV():
    def dfToCSV(self,dataframe,filename):

        # Check if the CSV fmotion already exists
        if os.path.exists(filename):
            # Append the DataFrame without the header_generated
            with open (filename,"a") as f:
                dataframe.to_csv(f, mode='a', header=False, index=False)
        else:
            # Write the DataFrame with the header_generated
            with open (filename,"w") as f:

                dataframe.to_csv(f, index=False)

    def dfToCSVHeader(self,dataframe,filename,header):

        # Check if the CSV fmotion already exists
        if os.path.exists(filename):
            # Append the DataFrame without the header_generated
            with open (filename, "a") as f:
                dataframe.to_csv(f, mode='a', header=False, index=False)
        else:
            with open (filename,"w") as f:
            # Write the DataFrame with the header_generated
                dataframe.to_csv(f, header=header,index=False)