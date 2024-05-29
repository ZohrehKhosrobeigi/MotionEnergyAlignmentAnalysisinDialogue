#THIS CLASS ROLL WINDOW ON NEGATIVE, POSITIVE, ANS ZERO LAG
import CreateLagsList
import SpearmanPostprocessing

class RollingLagSpearmanCorrelationComputation():

    def rollingLagSpearmanCorrelationComputation(self,onsetwin_var, offsetwin_var,n_lag,window_lenght_n_frame,windowlen_amountoflag_second,mELeft,mERight,wf_log,session, windowcount,
                                                  offset_in_sec_unit,leftId,rightId):
        wf=open("Error___Actual.txt", "a")

    # I USE SELF TO RETURN THE VALUES
        # iloc works with index and index which starts from 0 so, to access to first item_del i should use 0 and if I use index=1 it means the second item_del.
        # As a result start and end should be -1 to convert frame numbers as index numbers
        #NOTE here we use the frame numbers from 0 to the last.
        onsetwin_idx=onsetwin_var-1
        offsetwin_idx=offsetwin_var-1
        # create lags list
        crt_lags_lst = CreateLagsList.CreateLagsList ()
        crt_lags_lst.createLagsLst4Ramseyer (n_lag)
        lst_negative_lag = crt_lags_lst.lst_nagative_lags
        lst_positive_lag = crt_lags_lst.lst_positive_lags

##using dict created manually
        self.dict_a_window_info = {}
        self.dict_a_window_info["Session"]=session
        self.dict_a_window_info["LeftID"]=leftId
        self.dict_a_window_info["RightID"]=rightId
        self.dict_a_window_info["WindowNumber"] = windowcount
        self.dict_a_window_info["WindowOnset"] = onsetwin_var
        self.dict_a_window_info["WindowOffset"] = offsetwin_var
        self.dict_a_window_info["OffsetSecondUnit"] = offset_in_sec_unit

##############################################################################
        #########for lag -1

        max_frame = len (mELeft)

        for lag in lst_negative_lag:  # this section is for lag -
# here is for lag - on right side playerleft, means right playerleft is leading
            lagged_onset_idx = onsetwin_idx + ((window_lenght_n_frame * lag))
            lagged_offset_idx = lagged_onset_idx + window_lenght_n_frame - 1 # I use -1 to consider formula: end-start+1. So -1 keeps the lenght of windwo exactly the same as lenght of winodw
            # put all values 0 when the timestamps are zero

            if lagged_onset_idx < 0 or lagged_offset_idx > max_frame or onsetwin_idx < 0 or offsetwin_idx > max_frame:
                wf_log.write ("________\nThis is WINDOW number:   " + str (windowcount) + "  When RIGHT PLAYER is LEADING, but timestamps are out of range \n")

                wf_log.write ("__" + "\nThis is lag number:   " + str (lag * windowlen_amountoflag_second) + " When RIGHT PLAYER is LEADING, but timestamps are out of range\n")
                self.dict_a_window_info["Coeff_RightLeads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"]=0
                self.dict_a_window_info["Pval_RightLeads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"]=1
                self.dict_a_window_info["FisherZ_RightLeads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"]=0
                #addign used frame
                self.dict_a_window_info["RightFramesUsed_Leads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"]=[[0, 0]]


            else:
                motion_segment_ply_left = mELeft.iloc[onsetwin_idx:offsetwin_idx] # it is for current time of left playerleft, means lag 0, -----0----- # because iloc is not like list. to strart the considered frame, we should use -1. But for the end is ok. then the onset would be this index +1
                motion_segment_ply_right = mERight.iloc[lagged_onset_idx:lagged_offset_idx]
                spear_process=SpearmanPostprocessing.SpearmanProcessor()
                spear_process.spearmanProcess (motion_segment_ply_left, motion_segment_ply_right,wf)
                wf_log.write ("________\nThis is Window number:   " + str (windowcount) + "    for RIGHT PLAYER is LEADING, lagged windows are on right player and fix window is on left player \n")
                wf_log.write ("________\nThis is lag number:   " + str (lag * windowlen_amountoflag_second) + "    for RIGHT PLAYER is LEADING, lagged windows are on right player and fix window is on left player \n")
                wf_log.write ("\nThe onset of fix window (Left player), is:   " + str (onsetwin_idx) + "\n")
                wf_log.write ("\nThe offset of fix window(Left player), is:   " + str (offsetwin_idx) + "\n")
                wf_log.write ("\nThe onset of lagged window ( backward on Right player), is:   " + str (lagged_onset_idx) + "\n")
                wf_log.write ("\nThe offset of lagged window ( backward on Right player), is:   " + str (lagged_offset_idx) + "\n")
                wf_log.write ("\nThe  motion player  left, is:\n" + str (motion_segment_ply_left) + "\n")
                wf_log.write ("\nThe  motion player right ,is:  \n" + str (motion_segment_ply_right) + "\n")
                wf_log.write ("\nSpearman Coeffiecinet is:  \n" + str (spear_process.spear_coef) + "\n")
                wf_log.write ("\nPvalue is:  \n" + str (spear_process.pvalue_coef) + "\n__________")
                self.dict_a_window_info["Coeff_RightLeads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"] =spear_process.spear_coef
                self.dict_a_window_info["Pval_RightLeads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"] =spear_process.pvalue_coef
                self.dict_a_window_info["FisherZ_RightLeads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"] = spear_process.fisherz
                # addign used frame
                self.dict_a_window_info["RightFramesUsed_Leads_Lag_" + str(lag * windowlen_amountoflag_second) + "_second"] = [[lagged_onset_idx + 1, lagged_offset_idx + 1]]
#########################
# here is for lag - on left side player, means left player is leading

            # put all values 0 when the timestamps are zero

            if lagged_onset_idx < 0 or lagged_offset_idx > max_frame or onsetwin_idx < 0 or offsetwin_idx > max_frame:
                wf_log.write ("__" + "\nThis is Window number:   " + str (windowcount) + " When Left PLAYER is LEADING, but timestamps are out of range\n")

                wf_log.write ("__" + "\nThis is lag number:   " + str (lag * windowlen_amountoflag_second) + " When Left PLAYER is LEADING, but timestamps are out of range\n")
                self.dict_a_window_info["Coeff_LeftLeads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 0
                self.dict_a_window_info["Pval_LeftLeads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 1
                self.dict_a_window_info["FisherZ_LeftLeads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 0
                # addign used frame
                self.dict_a_window_info["LeftFramesUsed_Leads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = [[0, 0]]
            else:
                motion_segment_ply_right = mERight.iloc[onsetwin_idx:offsetwin_idx]  # it is for current time of right playerleft, means lag 0, -----0----- # because iloc is not like list. to strart the considered frame, we should use -1. But for the end is ok. then the onset would be this index +1
                motion_segment_ply_left = mELeft.iloc[lagged_onset_idx:lagged_offset_idx]
                spear_process = SpearmanPostprocessing.SpearmanProcessor ()
                spear_process.spearmanProcess (motion_segment_ply_left, motion_segment_ply_right,wf)
                wf_log.write ("________\nThis is Window number:   " + str (windowcount) + "    for LEFT PLAYER is LEADING, lagged windows are on LEFT player and fix window is on right player \n")

                wf_log.write ("________\nThis is lag number:   " + str (lag * windowlen_amountoflag_second) + "    for LEFT PLAYER is LEADING, lagged windows are on LEFT player and fix window is on right player \n")
                wf_log.write ("\nThe onset of fix window (Right player), is:   " + str (onsetwin_idx) + "\n")
                wf_log.write ("\nThe offset of fix window(Right player), is:   " + str (offsetwin_idx) + "\n")
                wf_log.write ("\nThe onset of lagged window ( backward on LEFT player), is:   " + str (lagged_onset_idx) + "\n")
                wf_log.write ("\nThe offset of lagged window ( backward on LEFT player), is:   " + str (lagged_offset_idx) + "\n")
                wf_log.write ("\nThe  motion player  left, is:\n" + str (motion_segment_ply_left) + "\n")
                wf_log.write ("\nThe  motion player right ,is:  \n" + str (motion_segment_ply_right) + "\n")
                wf_log.write ("\nSpearman Coeffiecinet is:  \n" + str (spear_process.spear_coef) + "\n")
                wf_log.write ("\nPvalue is:  \n" + str (spear_process.pvalue_coef) + "\n__________")
                self.dict_a_window_info["Coeff_LeftLeads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.spear_coef
                self.dict_a_window_info["Pval_LeftLeads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.pvalue_coef
                self.dict_a_window_info["FisherZ_LeftLeads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.fisherz
                # addign used frame
                self.dict_a_window_info["LeftFramesUsed_Leads_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = [[lagged_onset_idx + 1, lagged_offset_idx + 1]]
        ################# for lag 0

        motion_segment_ply_left = mELeft.iloc[onsetwin_idx: offsetwin_idx]
        motion_segment_ply_right = mERight.iloc[onsetwin_idx: offsetwin_idx]

        if onsetwin_idx < 0 or offsetwin_idx > max_frame or onsetwin_idx < 0 or offsetwin_idx > max_frame:
            wf_log.write ("__" + "\nThis is Window number:   " + str (windowcount) + " but timestamps are out of range\n")

            wf_log.write ("__" + "\nThis is lag number:   " + str (0) + " but timestamps are out of range\n")
            self.dict_a_window_info["Coeff_Lag_" + str (0) + "_second"] = 0
            self.dict_a_window_info["Pval_Lag_" + str (0) + "_second"] = 1
            self.dict_a_window_info["FisherZ_Lag_" + str (0) + "_second"] = 0
            # addign used frame
            self.dict_a_window_info["RightFramesUsed_Lag_" + str (0) + "_second"] = [[0, 0]]
            self.dict_a_window_info["LeftFramesUsed_Lag_" + str (0) + "_second"] = [[0, 0]]

        else:

            spear_process = SpearmanPostprocessing.SpearmanProcessor ()
            spear_process.spearmanProcess (motion_segment_ply_left, motion_segment_ply_right,wf)
          
            wf_log.write ("________\nThis is Window number:   " + str (windowcount) + "  for CO-PLAYERS \n")
            wf_log.write ("________\nThis is lag number:   " + str (0) + "  for CO-PLAYERS \n")
            wf_log.write ("\nThe onset of fix window (Right player), is:   " + str (onsetwin_idx) + "\n")
            wf_log.write ("\nThe offset of fix window(Right player), is:   " + str (offsetwin_idx) + "\n")
            wf_log.write ("\nThe onset of fix window (Left player), is:   " + str (onsetwin_idx) + "\n")
            wf_log.write ("\nThe offset of fix window(Left player), is:   " + str (offsetwin_idx) + "\n")
     
            wf_log.write ("\nThe  motion player  left, is:\n" + str (motion_segment_ply_left) + "\n")
            wf_log.write ("\nThe  motion player right ,is:  \n" + str (motion_segment_ply_right) + "\n")
            wf_log.write ("\nSpearman Coeffiecinet is:  \n" + str (spear_process.spear_coef) + "\n")
            wf_log.write ("\nPvalue is:  \n" + str (spear_process.pvalue_coef) + "\n__________")
            self.dict_a_window_info["Coeff_Lag_" + str (0) + "_second"] = spear_process.spear_coef
            self.dict_a_window_info["Pval_Lag_" + str (0) + "_second"] = spear_process.pvalue_coef
            self.dict_a_window_info["FisherZ_Lag_" + str (0) + "_second"] = spear_process.fisherz
            # addign used frame
            self.dict_a_window_info["LeftFramesUsed_Lag_" + str (0) + "_second"] = [[onsetwin_idx+1, offsetwin_idx+1]]
            self.dict_a_window_info["RightFramesUsed_Lag_" + str (0) + "_second"] = [[onsetwin_idx+1, offsetwin_idx+1]]

 ############################################################# for lag +
        for lag in lst_positive_lag:  # this section is for lag +

            # here is for lag + on right side player, means right player is following

            lagged_onset_idx = onsetwin_idx + ((window_lenght_n_frame * lag))
            lagged_offset_idx = lagged_onset_idx + window_lenght_n_frame - 1# I use -1 to consider formula: end-start+1. So -1 keeps the lenght of windwo exactly the same as lenght of winodw
            # put all values 9 when the timestamps are zero

            if lagged_onset_idx < 0 or lagged_offset_idx > max_frame or onsetwin_idx < 0 or offsetwin_idx > max_frame:
                wf_log.write ("__" + "\nThis is Window number: " + str (windowcount) + " When RIGHT PLAYER is Following, but timestamps are out of range\n")

                wf_log.write ("__" + "\nThis is lag number: " + str (lag * windowlen_amountoflag_second) + " When RIGHT PLAYER is Following, but timestamps are out of range\n")
    
                self.dict_a_window_info["Coeff_RightFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 0
                self.dict_a_window_info["Pval_RightFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 1
                self.dict_a_window_info["FisherZ_RightFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 0
                # addign used frame
                self.dict_a_window_info["RightFramesUsed_Follows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = [[0, 0]]

            else:
                motion_segment_ply_left = mELeft.iloc[onsetwin_idx:offsetwin_idx] # it is for current time of left playerleft, means lag 0, -----0----- # because iloc is not like list. to strart the considered frame, we should use -1. But for the end is ok. then the onset would be this index +1
                motion_segment_ply_right = mERight.iloc[lagged_onset_idx:lagged_offset_idx]
                spear_process = SpearmanPostprocessing.SpearmanProcessor ()
                spear_process.spearmanProcess (motion_segment_ply_left, motion_segment_ply_right,wf)

                wf_log.write ("________\nThis is Window number:   " + str (windowcount
                    ) + "    for RIGHT PLAYER is Following, lagged windows are on right player and fix window is on left player \n")
                wf_log.write ("________\nThis is lag number:   " + str (
                    lag) + "    for RIGHT PLAYER is Following, lagged windows are on right player and fix window is on left player \n")
                wf_log.write ("\nThe onset of fix window (Left player), is:   " + str (onsetwin_idx) + "\n")
                wf_log.write ("\nThe offset of fix window(Left player), is:   " + str (offsetwin_idx) + "\n")
                wf_log.write (
                    "\nThe onset of lagged window ( forward on Right player), is:   " + str (lagged_onset_idx) + "\n")
                wf_log.write ("\nThe offset of lagged window ( forward on Right player), is:   " + str (
                    lagged_offset_idx) + "\n")
                wf_log.write ("\nThe  motion player  left, is:\n" + str (motion_segment_ply_left) + "\n")
                wf_log.write ("\nThe  motion player right ,is:  \n" + str (motion_segment_ply_right) + "\n")
                wf_log.write ("\nSpearman Coeffiecinet is:  \n" + str (spear_process.spear_coef) + "\n")
                wf_log.write ("\nPvalue is:  \n" + str (spear_process.pvalue_coef) + "\n__________")
                self.dict_a_window_info["Coeff_RightFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.spear_coef
                self.dict_a_window_info["Pval_RightFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.pvalue_coef
                self.dict_a_window_info["FisherZ_RightFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.fisherz
                # addign used frame
                self.dict_a_window_info["RightFramesUsed_Follows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = [[lagged_onset_idx + 1, lagged_offset_idx + 1]]

         #######################
            # here is for lag + on left side playerleft, means left playerleft is following

            if lagged_onset_idx < 0 or lagged_offset_idx > max_frame or onsetwin_idx < 0 or offsetwin_idx > max_frame:

                wf_log.write ("___________________________________________________" + "\n")
                wf_log.write ("\nThis is Window number:   " + str (windowcount) + "    for LEFT PLAYER is FOLLOWING, but timestamps are out of range\n")

                wf_log.write ("\nThis is lag number:   " + str (lag * windowlen_amountoflag_second) + "    for LEFT PLAYER is FOLLOWING, but timestamps are out of range\n")
                wf_log.write ("__" + "\nThis is lag number:   " + str ( lag) + " When Left PLAYER is FOLLOWING, but timestamps are out of range\n")
                self.dict_a_window_info["Coeff_LeftFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 0
                self.dict_a_window_info["Pval_LeftFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 1
                self.dict_a_window_info["FisherZ_LeftFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = 0
                # addign used frame
                self.dict_a_window_info["LeftFramesUsed_Follows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = [[0, 0]]

            else:
                
                motion_segment_ply_right = mERight.iloc[onsetwin_idx:offsetwin_idx]  # it is for current time of left playerleft, means lag 0, -----0----- # because iloc is not like list. to strart the considered frame, we should use -1. But for the end is ok. then the onset would be this index +1
                motion_segment_ply_left = mELeft.iloc[lagged_onset_idx:lagged_offset_idx]
                spear_process = SpearmanPostprocessing.SpearmanProcessor ()
                spear_process.spearmanProcess (motion_segment_ply_left, motion_segment_ply_right,wf)
                wf_log.write ("________\nThis is Window number:   " + str (windowcount) + "    for LEFT PLAYER is Following, lagged windows are on LEFT player and fix window is on right player \n")

                wf_log.write ("________\nThis is lag number:   " + str (lag * windowlen_amountoflag_second) + "    for LEFT PLAYER is Following, lagged windows are on LEFT player and fix window is on right player \n")
                wf_log.write ("\nThe onset of fix window (Right player), is:   " + str (onsetwin_idx) + "\n")
                wf_log.write ("\nThe offset of fix window(Right player), is:   " + str (offsetwin_idx) + "\n")
                wf_log.write ( "\nThe onset of lagged window ( forward on LEFT player), is:   " + str (lagged_onset_idx) + "\n")
                wf_log.write ("\nThe offset of lagged window ( forward on LEFT player), is:   " + str (lagged_offset_idx) + "\n")
                wf_log.write ("\nThe  motion player  left, is:\n" + str (motion_segment_ply_left) + "\n")
                wf_log.write ("\nThe  motion player right ,is:  \n" + str (motion_segment_ply_right) + "\n")
                wf_log.write ("\nSpearman Coeffiecinet is:  \n" + str (spear_process.spear_coef) + "\n")
                wf_log.write ("\nPvalue is:  \n" + str (spear_process.pvalue_coef) + "\n__________")
                self.dict_a_window_info["Coeff_LeftFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.spear_coef
                self.dict_a_window_info["Pval_LeftFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.pvalue_coef
                self.dict_a_window_info["FisherZ_LeftFollows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = spear_process.fisherz
                # addign used frame
                self.dict_a_window_info["LeftFramesUsed_Follows_Lag_" + str (lag * windowlen_amountoflag_second) + "_second"] = [[lagged_onset_idx + 1, lagged_offset_idx + 1]]



##############
        # i use this to check if a header is missing or some if I want to add a new header is eaier to add. I add in Headername.py and then i add manually here and then in Erorr___txt I can check if something is wrong
        # key_dict_computed_headers_set = set (self.dict_a_window_info.keys ())
        # key_method_headers_set = set (dict_keys.keys ())
        # are_items_the_same = key_dict_computed_headers_set == key_method_headers_set
        # key_dict_computed_headers_set = set (self.dict_a_window_info.keys ())
        # key_method_headers_set = set (dict_keys.keys ())
        # # Determine items that are different
        # items_only_in_computed_headers = key_dict_computed_headers_set - key_method_headers_set
        # items_only_in_method_headers = key_method_headers_set - key_dict_computed_headers_set
        # wf.write("This will print True if keys of dictionaries are the same, and False otherwise.          "+str (are_items_the_same))
        # wf.write("\nthis is by me\n"+str(items_only_in_computed_headers)+"\n\n")
        # wf.write("\nthis is by method\n"+str(items_only_in_method_headers)+"\n\n")
        # # wf.write ("\nthis is by me all\n" + str (key_dict_computed_headers_set) + "\n\n")
        # # wf.write ("\nthis is by method all\n" + str (key_method_headers_set) + "\n\n")


        return self.dict_a_window_info

    #######################

