class CreateLagsList():
    def __init__(self):
        self.lst_nagative_lags=[]
        self.lst_positive_lags=[]

        self.lst_lags2plot=[]
        self.lst_lags_header_mean_sd=[]

    def createLagsLst4Boker(self,numberOfLags,stepOfLag):
        #This function creates a list of lags. I use this since I want to keep the lag zero. if I don't keep lag zero, sometime, during stepsize, lag zero is passed

        # # this for is for loop from negative step to the negative lenght of motion
        for i in range(-1, -(numberOfLags+1),-1):
            self.lst_nagative_lags.append(i * stepOfLag)
        self.lst_nagative_lags.reverse()

# numbr of lags for headers
        for i in range ((numberOfLags ),0, -1):
            self.lst_lags_header_mean_sd.append (-i )

# numbr of lags for plots
        for i in range ( -(numberOfLags ),1, 1):
            self.lst_lags2plot.append (i)

        for i in range ((numberOfLags ),0, -1):
            self.lst_lags2plot.append (i)


        return  self.lst_nagative_lags,self.lst_lags2plot,self.lst_lags_header_mean_sd
######################################

    def createLagsLst4Ramseyer(self,n_lag):
        #This function creates a list of lags. I use this since I want to keep the lag zero. if I don't keep lag zero, sometime, during stepsize, lag zero is passed

        # # this for is for loop from negative step to the negative lenght of motion
        for i in range(-1, -(n_lag + 1), -1):
            self.lst_nagative_lags.append(i )
        self.lst_nagative_lags.reverse()

#positive
        for i in range (1, n_lag + 1):
            self.lst_positive_lags.append(i)

# numbr of lags for headers
            # numbr of lags for headers
        for i in range (-1, -(n_lag + 1), -1):
            self.lst_lags_header_mean_sd.append (i )
        self.lst_lags_header_mean_sd.reverse ()


# numbr of lags for plots

        # numbr of lags for plots
        for i in range (-(n_lag), 1, 1):
            if i != 0:
                self.lst_lags2plot.append (i)

        for i in range (1, n_lag + 1):
            if i != 0:
                self.lst_lags2plot.append (i)

        return  self.lst_nagative_lags,self.lst_lags2plot,self.lst_lags_header_mean_sd


