# This class takes a csv file_Grid name and return rows of the file_Grid
import csv
class CSVReader():
    def __init__(self):
        self.lst_all_rows=[]
    def csvReader(self,inputfile):

        input_file = csv.DictReader(open(inputfile))

        #All df2_in2 is in this list
        for row in input_file:
            self.lst_all_rows.append(row)

        print(f'{inputfile} is read and added successfully')

        return self.lst_all_rows
