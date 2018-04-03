# input.dat is the data frame containing the absorbance data to be examined
# Data should be organized as column 52 =core depth, columns 1-51 = spectrophotometer wavelengths 650-700, measured every nm

chlA <- function(input.dat, details = F, na.rm = T){
  if(ncol(input.dat)!=52){
    print("Ensure that input data is formatted with 51 wavelength columns followed by 1 midpoint column.")
  } else{
    AOC <- numeric() # generating empty vectors for the loops later in the function
    AOL <- numeric()
    PA <- numeric()
    CHLA <- numeric()
    # Calculating the inferred chlorophyll a value for each interval (listed as rows)
    for(i in 1:nrow(input.dat)){
      AOC[i] <- sum(input.dat[i,1:51]) #Calculating the area under the curve
      AOL[i] <- (input.dat[i,1]*51)+(((input.dat[i,51]-input.dat[i,1])*51)/2) #calculating the area under the line
      PA[i] <- AOC[i]-AOL[i] #calculating the area under the peak
      CHLA[i] <- ((0.0919*PA[i])+0.0011) # calculating the chlorophyll a +derivatives inferred value
      print(paste("Calculating inferred chlorophyll a for the", input.dat[i, 52],"cm midpoint...")) # User feedback as the loop runs
    }
  }
  print(paste("Calculations complete for", nrow(input.dat), "intervals between", input.dat[1,52],"cm and", input.dat[nrow(input.dat),52],"cm!")) # User feedback to confirm the number of intervals processed
  output <- data.frame(Midpt = input.dat[,52], InfChlA = CHLA) #creating the output data frame
  # Give users the option to add units to the output in list form, or to have a simple data frame output without units listed.
  if(details==T){
    print("NOTE: For simple data frame output, set 'details' argument to FALSE.")
    return(list(output = output, Units = c(Midpt = "cm", InfChlA="mg/g dry weight"))) # Return the output data frame and units for each component to the user as the output of the function
  } else if(details ==F){
    print("NOTE: Midpt in cm and InfChlA in mg/g dry weight. To include units and output as an R list, set 'details' argument to TRUE.")
    return(output)
  }
}

chlA(dat, T)



dat <- read.csv(file=file.choose(), header =T, sep = ",", stringsAsFactors=FALSE, na.strings=c(""))
input.dat <- dat


