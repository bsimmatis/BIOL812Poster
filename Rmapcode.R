install.packages("extrafont")
library(extrafont)
font_import(pattern="icomoon", prompt=TRUE)

extrafont::loadfonts(device="pdf")
extrafont::loadfonts(device="postscript")
extrafont::loadfonts(device="win")
windowsFonts(icomoon=windowsFont("icomoon"))

install.packages("maps")
library(maps)

install.packages("mapdata")
library(mapdata)

install.packages("devtools")
library(devtools)

install.packages("ggplot2")
library(ggplot2)

install.packages("ggmap")
library(ggmap)

devtools::install_github("mikey-harper/ggmapstyles", force=TRUE)
library(ggmapstyles)

ggmap(get_snazzymap("Ottawa, Canada", zoom=8, mapRef = "https://snazzymaps.com/style/93/lost-in-the-desert"))+
  geom_text(aes(x=-75.6972,y=45.4215),label="Ottawa", nudge_y = 0.1, size = 5, family = "Calibri")+
  geom_text(aes(x=-74.634998,y=46.141313),label="Lac Duhamel",nudge_y=0.18,size=4.3, family = "Calibri")+
  geom_text(aes(x=-75.532051,y=46.458819),label="Lac-des-Iles",nudge_y=0.09,nudge_x=0.39,size=4.3, family = "Calibri")+
  geom_text(aes(x=-77.286973,y=44.477278),label="Stoco Lake",nudge_y=0.09,nudge_x=0.36,size=4.3, family = "Calibri")+
  geom_text(aes(x=-76.906359,y=45.677891),label="Muskrat Lake",nudge_y=0.18,size=4.3, family = "Calibri")+
  geom_text(aes(x=-76.4860,y=44.2312),label="Kingston", nudge_y = 0.12, size = 5, family = "Calibri")+
  geom_text(aes(x=c(-74.634998,-75.532051,-77.286973,-76.906359),y=c(46.141313,46.458819,44.477278,45.677891)),label=c("a","a","a","a"),family="icomoon",size=6,colour="red")+
  theme(axis.text.x = element_blank(),axis.text.y = element_blank(),axis.ticks = element_blank(),axis.title = element_blank())