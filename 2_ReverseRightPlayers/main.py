
#THIS CODE SORT SESSIONS ACCORING TO LENGHT. THEN MAKE A PAIR OF SESSIONS THAT THEIR DURATION IS CLOSE
# TO EACH OTHER. THEN, MAKE THEIR RIGH PLAYERS AS COPLAYERS AND ALSO, LEFT PLAYERS AS COPLAYERS.
# AND CHANGE THE NAME OF GESUTRE FILES TO ID AND SESSION OF THE PLAYER WITH NEW SESSION AND RIGHT OR LEFT SIDE PLAYER IS
#THE REAL SIDE OF THE PLAYER. SINCE WE CANNOT HAVE TWO RIGHT PLAYERS IN A SESSION. I MAKE ONE OF THEM LEFT AND THE OTHER ON RIGHT
#ALSO THE LENGTH OF GESTURE IS THE SAME AS LOWERE ONE.
import random
import time
import Importing_all_files_in_list_1
import Check_existed_folder_to_create_2
import CSV_DF_reader
import DFToCSV
import pandas as pd

# Seed the random number generator with the current time
random.seed(time.time())

# Specify paths to the input files for motion and gesture data
input_file_motion = "iOutput_Joint_ME_Coplayers_Norm_rMEA"
input_file_gest = "iCSV_Output_Gesture_Frame_Timestampe_PlayerSide"

# Define paths to the output directories for motion and gesture data
output_folderCSV_motion = "Output_ME_Reverse_RightSidePlayerFrames_rMEA"

output_folderCSV_gestt = "Output_Gest_Reverse_RightSidePlayerFrames_rMEA"

# Check and create output directory for motion data if it doesn't exist
finaloutputfolder = Check_existed_folder_to_create_2.createfolder()
finaloutputfolder.createfolder(output_folderCSV_motion)


# Check and create output directory for gesture data if it doesn't exist
finaloutputfolder = Check_existed_folder_to_create_2.createfolder()
finaloutputfolder.createfolder(output_folderCSV_gestt)


# Import and print all motion files
motion_files = Importing_all_files_in_list_1.importingfiles()
motion_files.get_candidates(input_file_motion)
print("*" * 100)
print(motion_files.filelist)
lst_files_motion = motion_files.filelist

# Import and print all gesture files
gest_files = Importing_all_files_in_list_1.importingfiles()
gest_files.get_candidates(input_file_gest)
print("*" * 100)
print(gest_files.filelist)
lst_files_gest = gest_files.filelist

# Find the smallest number of rows in motion data files
dict_df_motion_cut={}
for fmotion in lst_files_motion:
    csvdfreader = CSV_DF_reader.CSVDFReader()
    df_motion = csvdfreader.csvdfReader(fmotion)
    df_motion["MinMaxRightME"]=df_motion["MinMaxRightME"].iloc[::-1].values#revers motion of right side player
    #wrtie motion files in a new folder
    new_file_motion=fmotion.split("/")
    new_file_motion=output_folderCSV_motion+"/"+new_file_motion[-1]#write it in a new folder
    dftocsv = DFToCSV.DfToCSV ()
    dftocsv.dfToCSV (df_motion, new_file_motion)



    gestname_right= "iCSV_Output_Gesture_Frame_Timestampe_PlayerSide/" + df_motion["RightID"][1] + "_" + df_motion["Session"][1] + "_Gesture_Timestampes.csv"

    csvdfreader = CSV_DF_reader.CSVDFReader()
    csvdfreader.csvdfReader(gestname_right)
    df_gest_right= csvdfreader.df_motion
    df_gest_right["Is_Gesture"]=df_gest_right["Is_Gesture"].iloc[::-1].values#revers gestures of right side player
    df_gest_right["Gesture"]=df_gest_right["Gesture"].iloc[::-1].values#revers gestures of right side player


    new_file_gest=gestname_right.split("/")
    new_file_gest=output_folderCSV_gestt+"/"+new_file_gest[-1]#write it in a new folder
    dftocsv = DFToCSV.DfToCSV ()
    dftocsv.dfToCSV (df_gest_right, new_file_gest)

#writng left side player gesture as how it is
    gestname_right= "iCSV_Output_Gesture_Frame_Timestampe_PlayerSide/" + df_motion["LeftID"][1] + "_" + df_motion["Session"][1] + "_Gesture_Timestampes.csv"

    csvdfreader = CSV_DF_reader.CSVDFReader()
    csvdfreader.csvdfReader(gestname_right)
    df_gest_right= csvdfreader.df_motion

    new_file_gest=gestname_right.split("/")
    new_file_gest=output_folderCSV_gestt+"/"+new_file_gest[-1]
    dftocsv = DFToCSV.DfToCSV ()
    dftocsv.dfToCSV (df_gest_right, new_file_gest)