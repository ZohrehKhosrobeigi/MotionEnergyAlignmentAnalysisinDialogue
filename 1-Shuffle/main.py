import Importing_all_files_in_list_1
import Check_existed_folder_to_create_2
import CSV_DF_reader
import DFToCSV
import Shuffle
import PandaCSVReader

# Specify paths to the input files for motion and gesture data
input_file_motion = "iOutput_Joint_ME_Coplayers_Norm_rMEA"

# Define paths to the output directories for motion and gesture data
output_folderCSV_motion = "Output_ME_Shuffled_rMEA"

# Check and create output directory for motion data if it doesn't exist
finaloutputfolder = Check_existed_folder_to_create_2.createfolder()
finaloutputfolder.createfolder(output_folderCSV_motion)


# Import and print all motion files
motion_files = Importing_all_files_in_list_1.importingfiles()
motion_files.get_candidates(input_file_motion)
print("*" * 100)
print(motion_files.filelist)
lst_files_motion = motion_files.filelist



for file in lst_files_motion:
    print(file)
    motion_df = PandaCSVReader.PandaCSVReader ()
    motion_df.pandaCSVReader (file)
    shuffle=Shuffle.Shuffle()
    shuffle.shuffle(motion_df.df_data,"MinMaxRightME")

    dftocsv = DFToCSV.DfToCSV()
    output_file = output_folderCSV_motion+ "/" + file.split("/")[-1]
    dftocsv.dfToCSV(shuffle.df, output_file)
