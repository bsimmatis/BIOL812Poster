# For use with FullVRS files

# Write the results to a new .csv file
chlA.results <- read.csv("~/BIOL812Poster/chlorophyll.csv")

#Plot the chlorophyll a results
library(ggplot2)

ggplot(aes(x=InfChlA, y = Midpt), data=chlA.results)+
  geom_point(size=4.5)+
  scale_y_reverse()+
  theme_classic()+
  theme(text = element_text(size=18, face="bold"), 
        axis.text.x = element_text(colour="black", face="plain", size=16),
        axis.text.y = element_text(colour="black", face="plain", size=16))+
  xlab("Inferred Chlorophyll a (mg/g dry weight)")+
  ylab("Depth (cm)")
