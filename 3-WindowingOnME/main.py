#THIS CODE DOES ROLLING WINDOW WITH LAG AND PLOAT SEARMAN AND PVLAUE PER SESSION
#Leading and following for both players are computed.
import PandaCSVReader
import RollingWindow
import Importing_all_files_in_list_1
import GetName

##############
input_file = "iOutput_ME_Reversed_RightSidePlayerFrames_rMEA"
################
#lst_session_25fps = ["S09","S11"]
#####################################
#USIING ALGO 1, TO INTERPRET THE PLOTS, IF WE USE LAG 3, 5 AND 9, LAG 9, THE BIGEST NUMBER, CAN SHOW THE CC OF LAG 3 AND 5. SO
#COMPUTING LAG 3,5,9 IS REDUNDENCY SINCE LAG 9 INCLUDES ALL INFO.
lenght_of_lag = 0.3#for fps 30

fps=30
n_lag = 1
#######################################
temp=str(lenght_of_lag).replace(".", "")
output_folder= "W_"+temp+"_Output_Actual_Reversed"

#######################################
# Reading files from folder
files = Importing_all_files_in_list_1.importingfiles ()
files.get_candidates (input_file)
print ("*" * 100)
print (files.filelist)
lst_files=files.filelist

for file in lst_files:
    getname = GetName.GetName ()
    ply1, ply2, session, _ = getname.getName (file)
    motion_df = PandaCSVReader.PandaCSVReader ()
    motion_df.pandaCSVReader (file)
########################
     ################################### VIDEO
    rolling_window= RollingWindow.RollingWindow (
        motion_df.df_data["Session"][1], output_folder, fps, lenght_of_lag, n_lag,motion_df.df_data["LeftID"][1],motion_df.df_data["RightID"][1])  #len window is 5 second

    rolling_window.rollingWindow (motion_df.df_data["MinMaxLeftME"], motion_df.df_data["MinMaxRightME"],
                                  fps)  #if i pass right at first it should be wrong since the first var in the rolling class is for left playerleft.
    ##################
