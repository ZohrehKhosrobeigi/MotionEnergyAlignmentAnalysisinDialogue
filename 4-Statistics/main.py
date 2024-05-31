import SpearmanComputation
import SpearmanPostprocessing
import Importing_all_files_in_list_1
import PandaCSVReader
import PairingFiles
input_file="Data2Test/W_03_Output_Actual_rMEA_All_Pval/iOutput_Joint_ME_Coplayers_Norm_rMEA"
# input_file="Data2Test/W_03_Output_Reversed_rMEA_All_Pval/iOutput_ME_Reversed_RightSidePlayerFrames_rMEA"
# input_file="Data2Test/W_03_Output_Shuffled_rMEA_All_Pval/iOutput_ME_Shuffled_rMEA"
# input_file="Data2Test/W_03_Output_Actual_SSD_All_Pval/Output_Joint_ME_Coplayers_Norm_SSD"

wf = open ("Error___Actual.txt", "a")
# Reading files from folder
files = Importing_all_files_in_list_1.importingfiles ()
files.get_candidates (input_file)
print ("*" * 100)
print (files.filelist)
lst_files=files.filelist
#correlation between ME of co-players in entire session
for file in lst_files:
    motion_df = PandaCSVReader.PandaCSVReader ()
    motion_df.pandaCSVReader (file)
    spear_process = SpearmanPostprocessing.SpearmanProcessor ()
    spear_process.spearmanProcess (motion_df.df_data["MinMaxLeftME"],motion_df.df_data["MinMaxRightME"],wf)
    print("This is the correlation between co-players in entire session")
    print("this is file name:  ", file)
    print("This is rho:  ",spear_process.spear_coef,"This is p-value:  ",spear_process.pvalue_coef)

#Comparing OpenCV and rMEA, left side and righ side
lst_session = ["S02", "S03", "S04", "S05", "S07", "S08", "S09", "S10", "S11", "S13", "S14", "S17", "S18", "S19", "S20","S21", "S22", "S23"]

input_file_SSD="Data2Test/W_03_Output_Actual_SSD_All_Pval/Output_Joint_ME_Coplayers_Norm_SSD"
# Reading files from folder
files = Importing_all_files_in_list_1.importingfiles ()
files.get_candidates (input_file_SSD)
print ("*" * 100)
print (files.filelist)
lst_files_SSD=files.filelist
#Paring files of the same sessions from two different folders using session's number
paired_files=PairingFiles.PairingFiles()
paired_files.pairingFiles(lst_files,lst_files_SSD,lst_session)

for k,v in paired_files.dict_pairedfiles.items():

    motion_df_actual = PandaCSVReader.PandaCSVReader ()
    motion_df_actual.pandaCSVReader (v[0])

    motion_df_ssd = PandaCSVReader.PandaCSVReader ()
    motion_df_ssd.pandaCSVReader (v[1])
    print ("This is the correlation between left-side player extracted by MEA and  left-side player extracted by SSD-FDA  in entire session")
    spear_process = SpearmanPostprocessing.SpearmanProcessor ()
    spear_process.spearmanProcess (motion_df_actual.df_data["MinMaxLeftME"], motion_df_ssd.df_data["MinMaxLeftME"], wf)

    print ("this is file name:  ", v[0], v[1])
    print ("This is rho:  ", spear_process.spear_coef, "This is p-value:  ", spear_process.pvalue_coef)
    print()
    print ("This is the correlation between right-side player extracted by MEA and  right-side player extracted by SSD-FDA  in entire session")
    spear_process = SpearmanPostprocessing.SpearmanProcessor ()
    spear_process.spearmanProcess (motion_df_actual.df_data["MinMaxRightME"], motion_df_ssd.df_data["MinMaxRightME"], wf)

    print ("this is file name:  ", v[0], v[1])
    print ("This is rho:  ", spear_process.spear_coef, "This is p-value:  ", spear_process.pvalue_coef)

