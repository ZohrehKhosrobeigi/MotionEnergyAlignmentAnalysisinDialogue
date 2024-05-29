import random
import time

class Shuffle():
    def shuffle(self,df,header):
        # Seed the random number generator with the current time
        shuffled_values=df[header].tolist ()#keeping original values

        df[header]=0 #chage all values of the columns to zero to have no effect on sum and avg

        # Shuffle columns from motion dataframes, 10000 times shuffling
        for i in range (1,11):
            random.seed (time.time ())

            print(i)
            random.shuffle (shuffled_values)
            df[header] += shuffled_values# each time original values are shuffled and then add to the sum of last shulffed once.


        df[header]/=i #avg of shuffled values
        self.df=df

        return self.df





