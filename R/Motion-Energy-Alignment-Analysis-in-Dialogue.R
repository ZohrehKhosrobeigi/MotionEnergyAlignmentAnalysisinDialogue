#setwd("Data2Test/W_03_Output_Actual_rMEA_All_Pval/iOutput_Joint_ME_Coplayers_Norm_rMEA")
#setwd("Data2Test/W_03_Output_Shuffled_rMEA_All_Pval/iOutput_ME_Shuffled_rMEA")
#setwd("Data2Test/W_03_Output_Reversed_rMEA_All_Pval/iOutput_ME_Reversed_RightSidePlayerFrames_rMEA")
setwd("Data2Test/W_03_Output_Actual_SSD_All_Pval/Output_Joint_ME_Coplayers_Norm_SSD")
fisher_z_transform <- function(r) {
  return(0.5 * log((1 + r) / (1 - r)))
}
#CC btw co-players

# Get a list of all CSV files in the directory
file_list <- list.files(pattern="*.csv")

# Initialize an empty list to store results (optional)
results <- list()
p_values <- vector()
# Loop through each file
for (file in file_list) {
  # Read the CSV file
  DA <- read.csv(file, header=TRUE, stringsAsFactors=TRUE)
  # Perform the Spearman correlation test
  test_result <- with(DA, cor.test(MinMaxLeftME, MinMaxRightME, method="spearman"))
  p_values <- c(p_values, test_result$p.value)
  z_value <- fisher_z_transform(test_result$estimate)
  # Print the result (or store it)
  print(paste("Results for file:", file))
  print((test_result))
  
  print("Pvalue is")
  tempz<-test_result$p.value
  
  print(signif(tempz,5))
  
  print("  Rho ")
  print(signif(test_result$estimate,5))
  print("FisherZ")
  print(signif(z_value,5))
  print("*************************************")
  
}


# Apply Bonferroni Correction
number_of_tests <- length(p_values)
print(paste0("number_of_tests ",number_of_tests))

adjusted_alpha <- 0.05 / number_of_tests
print(paste0("Bonferroni adjustment to alpha: ",adjusted_alpha))    

adjusted_p_values <- p_values * number_of_tests

# Adjusting p-values to not exceed 1
adjusted_p_values <- pmin(adjusted_p_values, 1)

# Print or store the adjusted results
print("Bonferroni Adjusted P-Values:")
print(adjusted_p_values)


###############################
#Comparing OpenCV and rMEA
# Define the directories
dir1 <- "/Users/zohrehkhosrobeigi/PycharmProjects/MotionEnergyAlignmentAnalysisinDialogue/R/Data2Test/W_03_Output_Actual_rMEA_All_Pval/iOutput_Joint_ME_Coplayers_Norm_rMEA" 
dir2 <- "/Users/zohrehkhosrobeigi/PycharmProjects/MotionEnergyAlignmentAnalysisinDialogue/R/Data2Test/W_03_Output_Actual_SSD_All_Pval/Output_Joint_ME_Coplayers_Norm_SSD"



# List the files in each directory
files1 <- list.files(dir1, pattern="*.csv", full.names=TRUE)
files2 <- list.files(dir2, pattern="*.csv", full.names=TRUE)

# Check if both directories have the same number of files
if(length(files1) != length(files2)) {
  stop("The number of files in each directory does not match.")
}

# Initialize a list to store results
correlation_results <- list()

# Loop over the files in both directories simultaneously
for (i in 1:length(files1)) {
  

  # Read the files
  DOpen <- read.csv(files1[i], header=TRUE, stringsAsFactors=TRUE)
  DRMEA <- read.csv(files2[i], header=TRUE, stringsAsFactors=TRUE)
  
  # Calculate the correlations
  corr1 <- cor.test(DOpen$MinMaxLeftME, DRMEA$MinMaxLeftME, method="spearman")
  print(corr1)
  corr2 <- cor.test(DOpen$MinMaxRightME, DRMEA$MinMaxRightME, method="spearman")
  print(corr2)
}

###       ngram      ngram      ngram      ngram      ngram      ngram      ngram      ngram      ngram      

#Acutal and Reversed Per sessions

chisq.apr <- function(x,alpha) { # chi-squared adjusted pearson residuals N(0,1)
  print("********************")
  #print(x)
  
  print(chisq.test(x))
  #print("This is observation")
  #print(chisq.test(x)$observed)
  adjustedresiduals <- chisq.test(x)$stdres
  print("This is Residuals")
  print(signif(adjustedresiduals),4)
  #        return(chisq.test(x)$y)
  dim <- nrow(x)*ncol(x)
  p <- (alpha/dim) # bonferroni correction
  print(paste0("dimensions ","(",nrow(x),"x",ncol(x),"): ",dim))
  print(paste0("Bonferroni adjustment to alpha: ",p))    
  print(paste0("two-tailed critical value: ",qnorm(p/2,lower.tail=FALSE)))
  print("                                 ")
  if (chisq.test(x)$p.value<0.05)
    print(" It IS SIG")
  print("this is expection")
  print(chisq.test(x)$expected)
  
  
}

Da <- read.csv("Data2Test/W_03_Output_Actual_rMEA_All_Pval/FinalData_Actual_ME_Demog_rMEA_All_Pval/Aggregated_CC_WindowLength_0.3_Lag_3_Correlation_wins.csv",header=TRUE,stringsAsFactors=TRUE)
Dr <- read.csv("Data2Test/W_03_Output_Reversed_rMEA_All_Pval/FinalData_Reversed_ME_Demog_rMEA_All_Pval/Aggregated_CC_WindowLength_0.3_Lag_3_Correlation_wins.csv",header=TRUE,stringsAsFactors=TRUE)


bon<-0.05/32547
threshold<-0.05


Da$L0SigBin <- with(Da,ifelse(Pval_Lag_0_second<threshold,1,0))
Da$L0SigC <- factor(with(Da,ifelse(Pval_Lag_0_second<threshold,ifelse(Coeff_Lag_0_second<0,"Neg","Pos"),"Open")))


Dr$L0SigBin <- with(Dr,ifelse(Pval_Lag_0_second<threshold,1,0))
Dr$L0SigC <- factor(with(Dr,ifelse(Pval_Lag_0_second<threshold,ifelse(Coeff_Lag_0_second<0,"Neg","Pos"),"Open")))


#per session #Acutal and Reversed Per sessions
sessions <- unique(Da$Session)

for(session in sessions) {
  print("********************")
  print(session)
  session_d1<- subset(Da, Session == session)
  time_series_d1 <-session_d1$L0SigC
  # Initialize an empty vector to store 3-grams
  three_grams_d1 <- vector("list", length(time_series_d1) - 1)
  
  # Generate 3-grams
  for (i in 1:(length(time_series_d1) - 1)) {
    three_grams_d1[[i]] <- paste(time_series_d1[i], time_series_d1[i+1])
  }
  
  three_grams_vector_d1 <- unlist(three_grams_d1)
  Da3grams_d1 <- data.frame(ngrams = rep(NA, length(three_grams_vector_d1)))
  Da3grams_d1$ngrams <- three_grams_vector_d1
  Da3grams_d1$Resource <- factor(rep("D1", nrow(Da3grams_d1)))
  
  
  
  #Reversed
  
  session_d2 <- subset(Dr, Session == session)
  time_series_d2 <-session_d2$L0SigC
  # Initialize an empty vector to store 3-grams
  three_grams_d2 <- vector("list", length(time_series_d2) - 1)
  
  # Generate 3-grams
  for (i in 1:(length(time_series_d2) - 1)) {
    three_grams_d2[[i]] <- paste(time_series_d2[i], time_series_d2[i+1])
  }
  three_grams_vector_d2 <- unlist(three_grams_d2)
  Dr3grams_d2 <- data.frame(ngrams = rep(NA, length(three_grams_vector_d2)))
  Dr3grams_d2$ngrams <- three_grams_vector_d2
  Dr3grams_d2$Resource <- factor(rep("D2", nrow(Dr3grams_d2)))
  
  Dallgrams <- rbind(Da3grams_d1,Dr3grams_d2)
  Dallgrams$Resource <- as.factor(Dallgrams$Resource)
  Dallgrams$ngrams <- as.factor(Dallgrams$ngrams)
  
  # Now use xtabs for cross-tabulation without specifying a numeric count
  d1_counts <- with(Dallgrams, xtabs(~ ngrams + Resource))
  
  
  chisq.apr(d1_counts,0.05)
}


# Over sessions for Actual vs. Reversed

# Initialize Dallgrams outside the loop to collect data across all sessions
Dallgrams <- data.frame(ngrams = character(), Resource = factor())

# Iterate over sessions
for(session in unique(Da$Session)) {
  session_d1 <- subset(Da, Session == session)
  time_series_d1 <- session_d1$L0SigC
  three_grams_d1 <- vector("list", length(time_series_d1) - 1)
  
  for (i in 1:(length(time_series_d1) - 1)) {
    three_grams_d1[[i]] <- paste(time_series_d1[i], time_series_d1[i+1])
  }
  
  three_grams_vector_d1 <- unlist(three_grams_d1)
  Da3grams_d1 <- data.frame(ngrams = three_grams_vector_d1, Resource = factor(rep("Actual", length(three_grams_vector_d1))))
  
  session_d2 <- subset(Dr, Session == session)
  time_series_d2 <- session_d2$L0SigC
  three_grams_d2 <- vector("list", length(time_series_d2) - 1)
  
  for (i in 1:(length(time_series_d2) - 1)) {
    three_grams_d2[[i]] <- paste(time_series_d2[i], time_series_d2[i+1])
  }
  
  three_grams_vector_d2 <- unlist(three_grams_d2)
  Dr3grams_d2 <- data.frame(ngrams = three_grams_vector_d2, Resource = factor(rep("Shuffled", length(three_grams_vector_d2))))
  
  # Append to Dallgrams
  Dallgrams <- rbind(Dallgrams, Da3grams_d1, Dr3grams_d2)
}

# Aggregate Dallgrams to sum counts for each unique ngrams and Resource combination
Dallgrams$Count <- 1 # Add a count column for aggregation
DallgramsSum <- aggregate(Count ~ ngrams + Resource, data = Dallgrams, FUN = sum)

# Now DallgramsSum contains the summed counts for all ngrams and Resource combinations across all sessions
DallgramsSum$Resource <- as.factor(DallgramsSum$Resource)
DallgramsSum$ngrams <- as.factor(DallgramsSum$ngrams)

# Now use xtabs for cross-tabulation without specifying a numeric count
contingencyTable <- xtabs(Count ~ ngrams + Resource, data = DallgramsSum)
chisq.apr(contingencyTable,0.05)
####################################### End of Reversed


####################################### Actual vs. Shuffled

Da <- read.csv("Data2Test/W_03_Output_Actual_rMEA_All_Pval/FinalData_Actual_ME_Demog_rMEA_All_Pval/Aggregated_CC_WindowLength_0.3_Lag_3_Correlation_wins.csv",header=TRUE,stringsAsFactors=TRUE)
Dr <- read.csv("Data2Test/W_03_Output_Shuffled_rMEA_All_Pval/FinalData_Shuffled_ME_Demog_rMEA_All_Pval/Aggregated_CC_WindowLength_0.3_Lag_3_Correlation_wins.csv",header=TRUE,stringsAsFactors=TRUE)


bon<-0.05/32547
threshold<-0.05


Da$L0SigBin <- with(Da,ifelse(Pval_Lag_0_second<threshold,1,0))
Da$L0SigC <- factor(with(Da,ifelse(Pval_Lag_0_second<threshold,ifelse(Coeff_Lag_0_second<0,"Neg","Pos"),"Open")))


Dr$L0SigBin <- with(Dr,ifelse(Pval_Lag_0_second<threshold,1,0))
Dr$L0SigC <- factor(with(Dr,ifelse(Pval_Lag_0_second<threshold,ifelse(Coeff_Lag_0_second<0,"Neg","Pos"),"Open")))


#per session #Acutal and Shuffled Per sessions
sessions <- unique(Da$Session)

for(session in sessions) {
  print("********************")
  print(session)
  session_d1<- subset(Da, Session == session)
  time_series_d1 <-session_d1$L0SigC
  # Initialize an empty vector to store 3-grams
  three_grams_d1 <- vector("list", length(time_series_d1) - 1)
  
  # Generate 3-grams
  for (i in 1:(length(time_series_d1) - 1)) {
    three_grams_d1[[i]] <- paste(time_series_d1[i], time_series_d1[i+1])
  }
  
  three_grams_vector_d1 <- unlist(three_grams_d1)
  Da3grams_d1 <- data.frame(ngrams = rep(NA, length(three_grams_vector_d1)))
  Da3grams_d1$ngrams <- three_grams_vector_d1
  Da3grams_d1$Resource <- factor(rep("D1", nrow(Da3grams_d1)))
  
  
  
  #Shuffled
  
  session_d2 <- subset(Dr, Session == session)
  time_series_d2 <-session_d2$L0SigC
  # Initialize an empty vector to store 3-grams
  three_grams_d2 <- vector("list", length(time_series_d2) - 1)
  
  # Generate 3-grams
  for (i in 1:(length(time_series_d2) - 1)) {
    three_grams_d2[[i]] <- paste(time_series_d2[i], time_series_d2[i+1])
  }
  three_grams_vector_d2 <- unlist(three_grams_d2)
  Dr3grams_d2 <- data.frame(ngrams = rep(NA, length(three_grams_vector_d2)))
  Dr3grams_d2$ngrams <- three_grams_vector_d2
  Dr3grams_d2$Resource <- factor(rep("D2", nrow(Dr3grams_d2)))
  
  Dallgrams <- rbind(Da3grams_d1,Dr3grams_d2)
  Dallgrams$Resource <- as.factor(Dallgrams$Resource)
  Dallgrams$ngrams <- as.factor(Dallgrams$ngrams)
  
  # Now use xtabs for cross-tabulation without specifying a numeric count
  d1_counts <- with(Dallgrams, xtabs(~ ngrams + Resource))
  
  
  chisq.apr(d1_counts,0.05)
}


# Over sessions for Actual vs. Shuffled

# Initialize Dallgrams outside the loop to collect data across all sessions
Dallgrams <- data.frame(ngrams = character(), Resource = factor())

# Iterate over sessions
for(session in unique(Da$Session)) {
  session_d1 <- subset(Da, Session == session)
  time_series_d1 <- session_d1$L0SigC
  three_grams_d1 <- vector("list", length(time_series_d1) - 1)
  
  for (i in 1:(length(time_series_d1) - 1)) {
    three_grams_d1[[i]] <- paste(time_series_d1[i], time_series_d1[i+1])
  }
  
  three_grams_vector_d1 <- unlist(three_grams_d1)
  Da3grams_d1 <- data.frame(ngrams = three_grams_vector_d1, Resource = factor(rep("Actual", length(three_grams_vector_d1))))
  
  session_d2 <- subset(Dr, Session == session)
  time_series_d2 <- session_d2$L0SigC
  three_grams_d2 <- vector("list", length(time_series_d2) - 1)
  
  for (i in 1:(length(time_series_d2) - 1)) {
    three_grams_d2[[i]] <- paste(time_series_d2[i], time_series_d2[i+1])
  }
  
  three_grams_vector_d2 <- unlist(three_grams_d2)
  Dr3grams_d2 <- data.frame(ngrams = three_grams_vector_d2, Resource = factor(rep("Shuffled", length(three_grams_vector_d2))))
  
  # Append to Dallgrams
  Dallgrams <- rbind(Dallgrams, Da3grams_d1, Dr3grams_d2)
}

# Aggregate Dallgrams to sum counts for each unique ngrams and Resource combination
Dallgrams$Count <- 1 # Add a count column for aggregation
DallgramsSum <- aggregate(Count ~ ngrams + Resource, data = Dallgrams, FUN = sum)

# Now DallgramsSum contains the summed counts for all ngrams and Resource combinations across all sessions
DallgramsSum$Resource <- as.factor(DallgramsSum$Resource)
DallgramsSum$ngrams <- as.factor(DallgramsSum$ngrams)

# Now use xtabs for cross-tabulation without specifying a numeric count
contingencyTable <- xtabs(Count ~ ngrams + Resource, data = DallgramsSum)
chisq.apr(contingencyTable,0.05)
########### End of Shuffled


