mydat <- read.csv("~/BIOL812Poster/06-137FullVRS.csv", header = T) # Not sure how to soft-code this... need to run trhough each lake 
library(ggplot2)

# Combine all data into an easily plot-able three-column data frame
stackdat <- as.data.frame(cbind(mydat[,1], stack(mydat[,2:ncol(mydat)])))
names(stackdat) <- c("Freq", "Abs", "Int")

# Plot the actual points:

colfxn <- colorRampPalette(c("goldenrod", "blue"), bias =0.2)
DATcols <- colfxn(nlevels(stackdat$Int))

ggplot(aes(x = Freq, y = Abs), data = stackdat) + 
  geom_rect(aes(xmin=650, xmax=700, ymin=-Inf, ymax=Inf), fill = "grey80")+ # highlight the PAR for chl a
  geom_point(aes(colour=Int), pch = 16, alpha = 0.1, size = 2)+
  scale_colour_manual(values = DATcols, guide = F)+
  theme_classic()+
  xlab("Wavelength (nm)")+
  ylab("Absorbance Value")+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16))


# Plot 1: Outline plot (less ink)
ggplot(aes(x = Freq, y = Abs), data = stackdat) + 
  geom_rect(aes(xmin=650, xmax=700, ymin=-Inf, ymax=Inf), fill = "greenyellow")+ # highlight the PAR for chl a
  scale_colour_gradient(low="green",high="red")+
  stat_density_2d(aes(colour=..level..), size =1.25) + 
  theme_classic()+
  xlab("Wavelength (nm)")+
  ylab("Absorbance Value")+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16),
        legend.title = element_text(face="bold", size=12),
        legend.text= element_text(face="plain", size=10))

# Plot 2: Raster density plot (more ink, looks cooler)
ggplot(aes(x = Freq, y = Abs), data = stackdat) + 
  stat_density_2d(geom="raster", aes(fill=..density..), contour = F)+
  scale_fill_continuous(low="blue",high="yellow")+ 
  theme_classic()+
  xlab("Wavelength (nm)")+
  ylab("Absorbance Value")+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16),
        legend.title = element_text(face="bold", size=12),
        legend.text= element_text(face="plain", size=10))

## Isolating Photosynthetically Active Radiation (PAR) ##
# Refine PAR which is 400-700nm
PAR <- as.numeric(400:700)
PARdat <- mydat[which(mydat$Sample %in% PAR), ]
PARstackdat <- as.data.frame(cbind(PARdat[,1], stack(PARdat[,2:ncol(mydat)])))
names(PARstackdat) <- c("Freq", "Abs", "Int")

# Plot PAR data
# Plot 1: Outline plot (less ink)
ggplot(aes(x = Freq, y = Abs), data = PARstackdat) + 
  geom_rect(aes(xmin=650, xmax=700, ymin=-Inf, ymax=Inf), fill = "grey40")+ # highlight the PAR for chl a
  #geom_rect(aes(xmin=480, xmax=520, ymin=-Inf, ymax=Inf), fill = "grey80")+ # highlight the PAR for echinenone
  scale_colour_gradient(low="green",high="red")+
  stat_density_2d(aes(colour=..level..), size =1.25) + 
  theme_classic()+
  xlab("Wavelength (nm)")+
  ylab("Absorbance Value")+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16),
        legend.title = element_text(face="bold", size=12),
        legend.text= element_text(face="plain", size=10))

# Plot 2: Raster density plot (more ink, looks cooler)
ggplot(aes(x = Freq, y = Abs), data = PARstackdat) + 
  stat_density_2d(geom="raster", aes(fill=..density..), contour = F)+ #having fun with density fills
  scale_fill_continuous(low="blue",high="yellow")+ 
  theme_classic()+
  xlab("Wavelength (nm)")+
  ylab("Absorbance Value")+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16),
        legend.title = element_text(face="bold", size=12),
        legend.text= element_text(face="plain", size=10))

## Plot the actual points:
# Set the palette
colfxn <- colorRampPalette(c("goldenrod", "darkmagenta"), bias =0.2) # Set the top and bottom of the gradient
PARcols <- colfxn(nlevels(PARstackdat$Int)) # Number of colours = number of intervals

ggplot(aes(x = Freq, y = Abs), data = PARstackdat) + 
  geom_rect(aes(xmin=650, xmax=700, ymin=-Inf, ymax=Inf), fill = "grey80")+ # highlight the PAR for chl a
  geom_point(aes(colour=Int), pch = 16, alpha = 0.3, size = 3)+ # Points (lines won't work)
  scale_colour_manual(values = PARcols, guide_legend(title = "Midpoint (cm)"))+ # Add manual scale to improve look and interpretation
  theme_classic()+ # Bye-bye extra ink
  xlab("Wavelength (nm)")+
  ylab("Absorbance Value")+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16),
        legend.text = element_text(face="plain", size = 8), 
        #legend.position = "top",
        legend.title = element_text(face="bold", size = 12)) # Customizing the text size so it's legible on a poster

