import csv
import os
import pandas as pd

class CSVWriter():
    def csv_wrt_list(self,mylist,filename_csv,fieldnames):
        # csv header_generated
        # csv df2_in2
        file_exists = os.path.isfile (filename_csv)
        with open (filename_csv, 'a', newline='') as csvfile:
            writer = csv.DictWriter (csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader ()


            writer.writerow ({fieldnames[0]:mylist[0] ,fieldnames[1]: mylist[1], fieldnames[2]: mylist[2],fieldnames[3]: mylist[3]})


    def csv_wrt_dict(self, mydict, filename_csv,filename_ALL):
            # csv header_generated
            fieldnames = ['Session','Player','Number of Gesture','Gesture' ,'Onset','Offset']

            with open (filename_csv, 'w', newline='') as csvfile:
                writer = csv.DictWriter (csvfile, fieldnames=fieldnames)

                writer.writeheader ()

                for key,val in mydict.items():

                        writer.writerow ({'Session':val[0],'Player':val[1],'Number of Gesture': key,'Gesture':val[2], 'Onset':val[3] ,'Offset': val[4]})




            file_exists = os.path.isfile (filename_ALL)

            with open (filename_ALL, 'a', encoding='UTF8', newline='') as allf:
                fieldnames = ['Session', 'Player', 'Number of Gesture', 'Gesture', 'Onset', 'Offset']
                writer = csv.DictWriter (allf, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader ()
                for key,val in mydict.items():
                    writer.writerow ({'Session':val[0],'Player':val[1],'Number of Gesture': key,'Gesture':val[2], 'Onset':val[3] ,'Offset': val[4]})

    def dataCSVWriterHeader(self,data,header1 ,filename,is_header):

        if is_header:
            allspear = pd.DataFrame (data)
            allspear.to_csv (filename, header=header1,index=False)
        else:
            allspear = pd.DataFrame (data)
            allspear.to_csv (filename, header=False)


    def dataCSVWriter(self,data,header1 ,filename,is_header):

        file_exists = os.path.isfile (filename)
        if not file_exists:
            is_header=1
        else:
            is_header=0

        if is_header:
            allspear = pd.DataFrame (data)
            allspear.to_csv (filename, header=header1,index=False)
        else:
            allspear = pd.DataFrame (data)
            allspear.to_csv (filename, header=False)
#################################

    def csv_wrt_dict_auto(self,rows,filename):
        # csv header_generated
        fieldnames=[]
        for k,v in rows.items():
            fieldnames.append(k)

        # csv df2_in2
        file_exists = os.path.isfile (filename)

        with open (filename, 'a', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter (f, fieldnames=fieldnames,delimiter=",")
            if not file_exists:
                writer.writeheader ()

            writer.writerow (rows)
            #########################



##################################
    def csv_wrt_insted_list_auto(self, mylist, fieldnames, filename_csv):
        # csv header_generated
        # csv df2_in2
        file_exists = os.path.isfile (filename_csv)
        myfile = open (filename_csv, 'a')
        writer = csv.writer (myfile)

        if not file_exists:
            writer.writerow(fieldnames)
        for row in mylist:
            writer.writerow(row)


    def csv_wrt_lst_no_header(self, mylist, filename_csv):
        # csv header_generated
        # csv df2_in2
        myfile = open (filename_csv, 'a')
        writer = csv.writer (myfile)

        for row in mylist:
            writer.writerow(row)