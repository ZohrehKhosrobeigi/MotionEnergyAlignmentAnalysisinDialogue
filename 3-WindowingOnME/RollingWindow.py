# THIS CALSS RETURN THE DICT OF FRAMES THAT ARE USED AND WINDOWS OF CC AND TURN OF CC
# TO USE IN THE NEXT CLASS TO FIND FRAMES THAT ARE USED IN CC AND FIND THEIR CORRESPODING GESUTRE

# I drew the algorithm in my notebook


# note scipy computes correlation the same as R
# This IS THE ALGORITHM NUMBER 1 THE PICTURE IS IN MY NOTEBOOK


# <-------------------------------------------------MOTION PLAYER 1------------------------------------------------------->

# <-------------------------------------------------MOTION PLAYER 2------------------------------------------------------->
#  ---------------------------------------
#  -            WINDOW1                  -
#  -                                     -
# Phase 1                  #  ---------------------------------------
#  ---------------------------------------
#  -            LAG0                     -
#  -                                     -
#  ---------------------------------------
#  ---------------------------------------
#  -            LAG-1                    -
# Phase 2                         #  -                                     -
#  ---------------------------------------

#  ---------------------------------------
#  -            LAG-1                    -     Phase 3
#  -                                     -
#  ---------------------------------------


# this class compute rho for each window and its lags
# plot splited heatmap of turns
# plot rho each window, Window wise
# plot rho the same lags for windows, lag wise


# I handle the start and end of the boundries to do not go far or less that the len of motion
# I plot  lags and turns
# I convert useless values to the same values
# this algorithm works with frames not second
import json
import Check_existed_folder_to_create_2
import pandas as pd
import RollingLagSpearmanCorrelationComputation
import DFToCSV


class RollingWindow ():
    def __init__(self, session, outputfold, fps, windowlen_amountoflag, n_lag,leftId,rightId):
        self.windowlen_amountoflag_second = windowlen_amountoflag
        self.window_lenght_n_frame = int (self.windowlen_amountoflag_second * fps)
        # finetune parameters
        self.stepSizeWin = 10  # it is used to compute overlap
        self.n_lag = n_lag
        self.session = session
        self.leftId=leftId
        self.rightId=rightId
        self.outputperseesion = "Output_" + str (session) + "_WindowLength_" + str (
            windowlen_amountoflag) + "_Lag_" + str (self.n_lag)
        self.output_aggregated_session = outputfold + "/Aggregated_CC_WindowLength_" + str (
            windowlen_amountoflag) + "_Lag_" + str (n_lag)
        finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
        finaloutputfoler.createfolder (self.outputperseesion)
        finaloutputfoler = Check_existed_folder_to_create_2.createfolder ()
        finaloutputfoler.createfolder (self.output_aggregated_session)
        #####################
        self.name_CC_file_per_session = self.outputperseesion + "/" + str (session) + "_WindowLength_" + str (
            windowlen_amountoflag) + "_Lag_" + str (self.n_lag) + "_Correlation_wins.csv"
        wfname = self.name_CC_file_per_session.replace (".csv", ".txt")
        self.wf_log = open (wfname, "w")
        self.name_CC_file_aggregated_session = self.output_aggregated_session + "/" + "Aggregated_CC_WindowLength_" + str (
            windowlen_amountoflag) + "_Lag_" + str (self.n_lag) + "_Correlation_wins.csv"

    def rollingWindow(self, motionLeft, motionRight, fps):



        #  motion_df.df_data["Session"][1], output_folder, fps, lenght_of_lag, n_lag,motion_df.df_data["LeftID"][1],motion_df.df_data["RightID"][1]

        motionLeft = motionLeft.astype ('float64')
        motionRight = motionRight.astype ('float64')

        windowcount = 0
        # window rolling
        for fram_no in range (1, len (motionLeft) + 1, self.window_lenght_n_frame):


            self.wf_log.write ("------------------------------------\n")
            windowcount += 1
            # configs
            onsetWin = fram_no

            if onsetWin == 1:  # to avoid overlaping for the first window since it is zero it does not make sense to go backward
                onsetWin = fram_no
            else:
                # onsetWin= fram_no - overlap# use overlap to cover 1 qurt of frames as overlap
                onsetWin = fram_no



            offsetWin = onsetWin + self.window_lenght_n_frame - 1
            ###################
            if onsetWin > 0 and offsetWin < len (motionLeft):
                offset_in_sec_unit = offsetWin / fps

                rolling_lag_corr_compu = RollingLagSpearmanCorrelationComputation.RollingLagSpearmanCorrelationComputation ()
                rolling_lag_corr_compu.rollingLagSpearmanCorrelationComputation (onsetWin, offsetWin, self.n_lag,
                                                                                 self.window_lenght_n_frame,
                                                                                 self.windowlen_amountoflag_second, motionLeft,
                                                                                 motionRight, self.wf_log, self.session,
                                                                                 windowcount, offset_in_sec_unit, self.leftId,
                                                                                 self.rightId)

                df = pd.DataFrame (rolling_lag_corr_compu.dict_a_window_info)

                # Select columns with names containing "FramesUsed_Lag_"
                selected_cols = df.filter (like='FramesUsed_Lag_').columns

                # Apply json.dumps elementwise to selected columns
                # df[selected_cols] = df[selected_cols].applymap (json.dumps)
                for col in selected_cols:
                    df[col] = df[col].apply (json.dumps)

                df2csv = DFToCSV.DfToCSV ()

                df2csv.dfToCSV (df, self.name_CC_file_per_session)

                df2csv.dfToCSV (df, self.name_CC_file_aggregated_session)


