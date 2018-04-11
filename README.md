# Broadening the spectra: looking beyond VRS-inferred chlorophyll a (650-700nm) to identify changes in whole-lake primary production
## Repository for BIOL812 Poster
## Authors: C Juurakko, N Kharazian, S Knebel, B Simmatis, L Simmatis
##### PLEASE DO NOT DISTRIBUTE DATA; DATA NOT PUBLISHABLE
### This repository was designed to store images, code and related information to generate a data poster for BIOL812 at Queen's University.

#### Purpose and Organization of Repository
We aim to determine whether:
1. Chlorophyll a changes over time in each lake and, 
2. Whether we can “fingerprint” deep vs shallow eutrophic lakes, and, if so, whether the differences correlate to the wavelengths of known specific pigments.
  
This repository includes R and Python code to address these questions, depending on the component. All data, images and text files were uplodaded using Git bash.

#### Our Four Focal Lakes
1. Stoco Lake was classified as eutrophic (spring TP ranged from 30-50 µg·L-1) until sewage management upgrades were installed in the late 1980’s. Currently, the lake is mesotrophic (spring TP ~15 µg·L-1, maximum depth 12m), though cyanobacterial blooms and excessive summer algal growth still occur frequently, likely due to the internal loading of phosphorus from the sediments.
2. Lac Duhamel (maximum depth 26m; oligotrophic, summer TP <4 μg∙L-1) is located upstream of Mont Tremblant, Quebec, has records of high human impact, including forestry and highway road salt application. It is extremely sensitive to cultural eutrophication, primarily due to the channelization of its tributaries, Shield bedrock, and long water residence time of 2 years (Biofilia, 2004). 
3. Lac-des-Îles (maximum depth 37m) is located on the Canadian Shield near Mont-Laurier, Quebec, and is classified as oligo-mesotrophic (summer TP ~10.5 μg∙L-1; Enviro’Eau, 2009). The lake supports a variety of sports fish, including lake trout, and is generally considered environmentally sensitive to eutrophication due to its relatively low nutrient levels. 
4. Muskrat Lake (maximum depth 60m) is valued for its recreational use and as a drinking water source for the town of Cobden, Ontario, located at the south end of the lake. High total phosphorus (>40 μg/L), low water clarity, and algal blooms have raised water quality concerns, largely attributed to eutrophication from heavy agricultural watershed development.

#### Data Collection and Content
Paleolimnological approaches use a variety of biological, physical and chemical indicators preserved in lake sediments to reconstruct past environmental conditions (Smol, 2008). Visible range spectroscopy (VRS) can track past changes in whole lake primary production by tracking sedimentary chlorophyll a and its degradation products, providing information on shifts in lake trophic status (Michelluti et al., 2010). Most cores were collected and had the sediment-water interface stabilized with Zorbitol© before refrigerated shipment to Université Laval, Laval, QC. Cores were then split and stored in a cold room (<4°C) prior to shipment to PEARL, Queen’s University, Kingston, ON. Individual intervals of freeze-dried sediment have been dated via gamma spectroscopy at Queen’s University using unsupported 210Pb activities in a constant rate of supply (CRS) model (Appleby and Oldfield, 1978; Binford 1990). Freeze-dried sediments have been sieved (120µm mesh) and sub-sampled such that a 50mL glass scintillation vial has at least 1mm of sediment. The sediments have been scanned through the base of the glass vials using a Rapid Content Analyzer (FOSS NIRSystems Inc.) operating over a range of 400-2,500 nm.
  
The data is comprised of a series of absorbance values from 400-2,500nm through time, which broadly represents the proportion of organic matter in the sediment. The absorbance values demonstrate the type of algae present in the lake depending on where absorbance peaks through the spectra (e.g. chlorophyll a is expected to occur between 650-700nm, representing whole-lake primary production). Each sediment interval has 2100 values and each lake core can have over 30 intervals of sediment stored in 2D datasets. Our largest data set, Muskrat Lake, has 71 intervals of sediment with 2100 values per interval for a total of ~72 000 data points. 

The simulated data was generated according to a variation on Agent-based modelling (ABM) that is commonly used in ecology, referred to as invidivual-based modelling (IBM). In particular, using a modified game theoretical model, the parameter of resource division was used to simulate the evolution of an algae population in a lake according to individual behavior. The data obtained was used to make predictions about how an enviroment may change with respect to Chlorophyll a, given certain environmental conditions and an initial measure of Chlorophyll a.

#### Data Included in this Repository:
* Dating profiles for each sediment core, which was generated using a constant rate of 210-Pb supply model via ScienTissiME
* Full spectrum absorbance values for four lakes
* "Chlorophyll a" spectrum (650-700nm) absorbance values for four lakes
* Location information for the focal lakes

[STEF'S INFO HERE]

#### Code Included in this Repository:
* Custom Chlorophyll a function
* Chlorophyll a plot codes (using ggplot2 in R)
* Full wavelength range codes, with plot options for raw data, density, and raster images (using ggplot2 in R)
* Code to generate map of sediment cores
* [LEIF'S INFO HERE]
* [STEF'S INFO HERE]

### References
1. Appleby, P.G., and Oldfield, F. 1978. The calculation of lead-210 dates assuming a constant rate of supply of unsupported 210Pb to the sediment. Catena, 5:1-8.
2. Binford, M. 1990. Calculation and uncertainty analysis of 210Pb dates for PIRLA project lake sediment cores. Journal of Paleolimnology, 3(3): 253-267.
3. Biofilia (Consultants en Environnement). 2004. Diagnose de basin versant: Lac Duhamel, Ville de Mont-Tremblant. Rapport final (only available in French), URL: http://lacduhamel.ca/wp-content/uploads/2015/09/diagnose-bassin-versant.pdf, accessed 15 Nov 2017. 
4. Enviro’Eau (Services-Conseils). 2009. Diagnose du Lac- des- Îles: Municipalité de Sain-Aimé-du-Lac-des- Îles et Ville de Mont-Laurier, Québec. Rapport final (only available in French), URL: www.villemontlaurier.qc.ca/DATA/DOCUMENT/Rapport et annexes-diagnose lac des Îles-2009.pdf, accessed 9 Nov 2017.
5. Michelutti, N., Blais, J.M., Cumming, B.F., Paterson, A.M., Rühland, K., Wolfe, A.P., and Smol, J.P. 2010. Do spectrally inferred determinations of chlorophyll a reflect trends in lake trophic status? Journal of Paleolimnology, 143: 205–217.
