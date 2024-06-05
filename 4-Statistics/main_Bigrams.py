# this code lables each window and defines bigrams of labled windows
import ChiSquaredTest
import PandaCSVReader
import BigramsLabeling
import pandas as pd
threshold = 0.05

input_file_actual= "Data2Test/W_03_Output_Actual_rMEA/Aggregated_CC_WindowLength_0.3_Lag_1/Aggregated_CC_WindowLength_0.3_Lag_1_Correlation_wins.csv"
input_file_reversed= "Data2Test/W_03_Output_Reversed_rMEA/Aggregated_CC_WindowLength_0.3_Lag_1/Aggregated_CC_WindowLength_0.3_Lag_1_Correlation_wins.csv"
input_file_shuffled= "Data2Test/W_03_Output_Actual_Shuffled/Aggregated_CC_WindowLength_0.3_Lag_1/Aggregated_CC_WindowLength_0.3_Lag_1_Correlation_wins.csv"
wf=open("Results.txt","w")
motion_df = PandaCSVReader.PandaCSVReader ()
df_actual=motion_df.pandaCSVReader (input_file_actual)

motion_df = PandaCSVReader.PandaCSVReader ()
df_reversed=motion_df.pandaCSVReader (input_file_reversed)


motion_df = PandaCSVReader.PandaCSVReader ()
df_shuffled=motion_df.pandaCSVReader (input_file_shuffled)


# Get unique sessions
sessions = df_actual['Session'].unique()
#Bigram per session Actual vs. Reversed
wf.write("Per session Actual vs. Reversed")
for session in sessions:
    wf.write ("\n********************\n")
    wf.write (session)
    bigrams_labeling=BigramsLabeling.BigramsLabeling()
    bigrams_labeling.bigrmasLabeling(df_actual,df_reversed,threshold,session)
    d1_counts = pd.crosstab (bigrams_labeling.df_all_grams['ngrams'], bigrams_labeling.df_all_grams['Resource'])
    chi_test=ChiSquaredTest.ChiSquaredTest()
    chi_test.chiSquaredTest(d1_counts,wf)
wf.write ("\n\nENd of  Per session Actual vs. Reversed\n\n")


#Bigram Aggregated session Actual vs. Reversed
wf.write("\nPer session Actual vs. Reversed\n")
df_allgrams = pd.DataFrame (columns=['ngrams', 'Resource'])
for session in sessions:
    wf.write ("\n********************\n")
    wf.write (session)
    bigrams_labeling=BigramsLabeling.BigramsLabeling()
    bigrams_labeling.bigrmasLabeling(df_actual,df_reversed,threshold,session)
    df_allgrams=pd.concat([df_allgrams,bigrams_labeling.df_all_grams], ignore_index=True)
# Aggregate Dallgrams to sum counts for each unique ngrams and Resource combination
df_allgrams['Count'] = 1  # Add a count column for aggregation
DallgramsSum = df_allgrams.groupby (['ngrams', 'Resource']).sum ().reset_index ()
# Create contingency table
contingency_table = pd.pivot_table (DallgramsSum, values='Count', index='ngrams', columns='Resource', fill_value=0)
# Perform Chi-square test
chi_test=ChiSquaredTest.ChiSquaredTest()
chi_test.chiSquaredTest(contingency_table,wf)
wf.write ("\n\nENd of  Aggregated session Actual vs. Reversed\n")
####################################   Actual vs. Shuffled



#Bigram per session Actual vs. Reversed
wf.write("Per session Actual vs. Shuffled")
for session in sessions:
    wf.write ("\n********************\n")
    wf.write (session)
    bigrams_labeling=BigramsLabeling.BigramsLabeling()
    bigrams_labeling.bigrmasLabeling(df_actual,df_shuffled,threshold,session)
    d1_counts = pd.crosstab (bigrams_labeling.df_all_grams['ngrams'], bigrams_labeling.df_all_grams['Resource'])
    chi_test=ChiSquaredTest.ChiSquaredTest()
    chi_test.chiSquaredTest(d1_counts,wf)
wf.write ("\n\nENd of  Per session Actual vs. Shuffled\n\n")


#Bigram Aggregated session Actual vs. Shuffled
wf.write("\nPer session Actual vs. Shuffled\n")
df_allgrams = pd.DataFrame (columns=['ngrams', 'Resource'])
for session in sessions:
    wf.write ("\n********************\n")
    wf.write (session)
    bigrams_labeling=BigramsLabeling.BigramsLabeling()
    bigrams_labeling.bigrmasLabeling(df_actual,df_shuffled,threshold,session)
    df_allgrams=pd.concat([df_allgrams,bigrams_labeling.df_all_grams], ignore_index=True)
# Aggregate Dallgrams to sum counts for each unique ngrams and Resource combination
df_allgrams['Count'] = 1  # Add a count column for aggregation
DallgramsSum = df_allgrams.groupby (['ngrams', 'Resource']).sum ().reset_index ()
# Create contingency table
contingency_table = pd.pivot_table (DallgramsSum, values='Count', index='ngrams', columns='Resource', fill_value=0)
# Perform Chi-square test
chi_test=ChiSquaredTest.ChiSquaredTest()
chi_test.chiSquaredTest(contingency_table,wf)
wf.write ("\n\nENd of  Aggregated session Actual vs. Shuffled\n")