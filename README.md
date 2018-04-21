# Broadening the spectra: looking beyond VRS-inferred chlorophyll a (650-700nm) to identify changes in whole-lake primary production
## Repository for BIOL812 Poster
## Authors: C Juurakko, S Knebel, B Simmatis, L Simmatis
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

##### Field Work Data
Paleolimnological approaches use a variety of biological, physical and chemical indicators preserved in lake sediments to reconstruct past environmental conditions (Smol, 2008). Visible range spectroscopy (VRS) can track past changes in whole lake primary production by tracking sedimentary chlorophyll a and its degradation products, providing information on shifts in lake trophic status (Michelluti et al., 2010). VRS-inferred chlorophyll a is calculated using the following equation:
  
[chlorophyll *a* + derivatives] = 0.0919$\times$peak area*~650-700nm~*+0.0011
  
Most cores were collected and had the sediment-water interface stabilized with Zorbitol© before refrigerated shipment to Université Laval, Laval, QC. Cores were then split and stored in a cold room (<4°C) prior to shipment to PEARL, Queen’s University, Kingston, ON. Individual intervals of freeze-dried sediment have been dated via gamma spectroscopy at Queen’s University using unsupported 210-Pb activities in a constant rate of supply (CRS) model (Appleby and Oldfield, 1978; Binford 1990). Freeze-dried sediments have been sieved (120µm mesh) and sub-sampled such that a 50mL glass scintillation vial has at least 1mm of sediment. The sediments have been scanned through the base of the glass vials using a Rapid Content Analyzer (FOSS NIRSystems Inc.) operating over a range of 400-2,500 nm.
  
The data is comprised of a series of absorbance values from 400-2,500nm through time, which broadly represents the proportion of organic matter in the sediment. The absorbance values demonstrate the type of algae present in the lake depending on where absorbance peaks through the spectra (e.g. chlorophyll a is expected to occur between 650-700nm, representing whole-lake primary production). Each sediment interval has 2100 values and each lake core can have over 30 intervals of sediment stored in 2D datasets. Our largest data set, Muskrat Lake, has 71 intervals of sediment with 2100 values per interval for a total of ~72 000 data points. 

##### Simulated Data
We have created a mathematical model, the Enhanced Ultimatum Game, and have written a script in python
of the model. The simulation may be used to predict how an algae population will evolve and, in turn, how
much chlorophyll a we may expect.

###### 1 What is the Ultimatum Game (UG)?
The Ultimatum Game (UG) is a game theoretical model that involves two players, the proposer and the responder, that must divide a resource between them. The proposer first "offers" an amount to the responder. If the responder "accepts" the
offer then the resource is divided according to the proposal. If the offer is "rejected" then both players walk
away with nothing.

Here, we investigate a new UG theoretical model, the Enhanced Ultimatum Game (EUG) where we introduce a cost associated with a demand.
In the EUG, the responder takes on an additional role as the demander. In
this version, the responder first makes a demand for how to divide the resources and the proposer will then
make an offer. The responder will then accept, with a cost, or reject.

In the case of an algae population, there is limited resource available within an environment which is to be
divided among the algae. There exists competition for resources and certain types of algae will be more
likely to succeed given particular enviroments. The UG model provides a method for classifying types of
algae and how interaction may evolve the population. For instance, let’s consider surface area of an alga X 
and suppose one of the resources to be divided is sunlight. Suppose X has the largest surface area compared
to other members in the population. Since surface area will play a large role in dictating the amount of
nutrients algae may absorb from the sun, X is at an advantage in this regard. We may interpret X as having a
high Demand. Next suppose X is shaded from the sun for a finite amount of time. If X has some other means
of obtaining necessary nutrients then it will continue to thrive. We may interpret X as having a low Min
accept. X then has the best strategy and is more likely to survive and dominate a population.

The EUG incorporates a demand and cost into the game and is played between two participants as follows:

- There are n resources to be divided
- The responder demands an amount d such that 0 < d < n
- The proposer then makes an offer p
- The responder has a minimum M that they are willing to accept and it must be that M <= d
- There is a cost to the responder when d != M. The cost is c(d−M) where c > 0
- If p <= M then the resources are divided accordingly. If p > M then both receive zero resources

For this project, we are interested in the amount of chlorophyll a within a lake and so, for the simulation, algae will
act as the players in the EUG model. Also, several factors influence the evolution of chlorophyll in an algae
population (ie. nutrients, sunlight, total phosphate etc). For instance, Total Phosphate (TP) found within
a lake is thought to influence the quantity of a type of algae and sun exposure is associated with specific
chlorophyll types. Therefore, for the purposes of this project, one may view TP and sunlight exposure as the
resource to be divided in the EUG model. This will allow us to make predictions about the group research
question: Whether the quantity of Chlorophyll a changes over time in a lake, given a particular environment.

###### 2 Brief description of simulation
The simulated data will be generated according to a variation on Agent-based modelling (ABM) that is
commonly used in ecology, referred to as invidivual-based modelling (IBM). In particular, we shall use
the parameter of resource division to simulate the evolution of an algae population in a lake according to
individual behavior. The data obtained will be used to make predictions about how an enviroment may
change with respect to chlorophyll a, given certain environmental conditions and an initial measure of
chlorophyll a.

###### 3 What are the parameters?
Below is a list of the more interesting ways the simulation was altered:
- Created a data set from various distributions (ie. poisson distribution and varied lambda)
- Varied the cost parameter (ie. instead of n(D-MA) for some n>0, I tried n(D-2P+MA) for some n>0
etc).
- Introduced a resource probability parameter such that the resource available to any one alga would
vary according to a normal distribution.
- Created an algae-type parameter (based on chlorophyll a vs. b) that was associated with proposal
values.

For the graph displayed on the poster, the following parameters were used:
- resource = 20 (Amount of resource to be divided)
- cost = 2 (Cost for demanding more than MA)
- runs = 10 (Number of interactions)
- popsize = 500 (population size/Number of algae)
- generations = 500 (Number of generations)
- tsize = 4 (Tournament size)
- pmr=0.05 (Point mutation rate for proposal)
- mdr=0.5 (Point mutation rate for demand and MA)
- epoch=5

###### 4 Algorithm/psuedocode
Below is a outline/description of the python code:
1. Import necessary packages (numpy and matplotlib.pyplot)
2. Define variables (resource, cost, runs, popsize, generations, tsize, pmr, mdr, epoch)
3. Create main loop.
    1. Create characteristics of population: create an array for each alga within the population.
Within each array describes the structure of the alga. The array contains 23 cells
[3,4,2,6,2,14,15,13,2,6,7,8,6,4,3,3,7,8,9,9,7,18,0]. The first 20 cells correspond to proposal values that
the alga will make, dependent on the demands. For example, if a second agla demands 3, then the
first alga will propose the amount found in the 4th cell of the array. If the second alga demands 4,
then the first alga will propose the amount found in the 5th cell of its array, and so on. The 21st
cell is the alga’s minaccept value, the 22nd is it’s demand value, and the 23rd slot is it’s fitness
score. Suppose there is a population of n algae then n 23 celled arrays are created.
    2. Population interacts: Have each member of the population interact with all other members of the
population twice, once as the demander and again as the proposer. Calculate and append fitness
scores. Continue for g generations.
    3. Point mutation: Pull out a few members of the population, choose the two members with the highest
fitness scores and have them produce two "offspring" that will replace two existing algae that have
the lowest fitness scores.
    4. Stats: calculate average, minimum and maximum fitness scores across epochs
    5. Plot: Create graph of maximum, minimum, and average fitness scores vs epoch

###### 5 How were the parameters varied?
For the graph displayed on the poster, all values found in the section of this paper titled “What are the
parameters” were varied. However, I eventually fixed most values, as mentioned, except for the “runs”,
“generations” and “epochs” variables. I varied the parameters within the range that the memory of my
computer would allow (approx. 0 - 100,000 units).

#### Data Included in this Repository:
* Dating profiles for each sediment core, which was generated using a constant rate of 210-Pb supply model via ScienTissiME
* Full spectrum absorbance values for four lakes
* "Chlorophyll a" spectrum (650-700nm) absorbance values for four lakes
* Location information for the focal lakes
* Simulated data of algae population


#### Code Included in this Repository:
* Custom Chlorophyll a function
* Chlorophyll a plot codes (using ggplot2 in R)
* Full wavelength range codes, with plot options for raw data, density, and raster images (using ggplot2 in R)
* Code to generate map of sediment cores
* Simulation: Python code for game theoretical mathematical model. 

### References
1. Appleby, P.G., and Oldfield, F. 1978. The calculation of lead-210 dates assuming a constant rate of supply of unsupported 210Pb to the sediment. Catena, 5:1-8.
2. Binford, M. 1990. Calculation and uncertainty analysis of 210Pb dates for PIRLA project lake sediment cores. Journal of Paleolimnology, 3(3): 253-267.
3. Biofilia (Consultants en Environnement). 2004. Diagnose de basin versant: Lac Duhamel, Ville de Mont-Tremblant. Rapport final (only available in French), URL: http://lacduhamel.ca/wp-content/uploads/2015/09/diagnose-bassin-versant.pdf, accessed 15 Nov 2017.
4. Bohl, Katrin, Sabine Hummert, Sarah Werner, David Basanta, Andreas Deutsch, Stefan Schuster, and Anja
Schroeter. 2014. “Evolutionary Game Theory: Molecules as Players.” Mol. BioSyst. 10 (12). Royal Society
of Chemistry (RSC): 3066–74. doi:10.1039/c3mb70601j.
5. Carlson, R.E. and J. Simpson. 1996. A Coordinator’s Guide to Volunteer Lake Monitoring Methods. North
American Lake Management Society. 96 pp.
6. Enviro’Eau (Services-Conseils). 2009. Diagnose du Lac- des- Îles: Municipalité de Sain-Aimé-du-Lac-des- Îles et Ville de Mont-Laurier, Québec. Rapport final (only available in French), URL: www.villemontlaurier.qc.ca/DATA/DOCUMENT/Rapport et annexes-diagnose lac des Îles-2009.pdf, accessed 9 Nov 2017.
7. Michelutti, N., Blais, J.M., Cumming, B.F., Paterson, A.M., Rühland, K., Wolfe, A.P., and Smol, J.P. 2010. Do spectrally inferred determinations of chlorophyll a reflect trends in lake trophic status? Journal of Paleolimnology, 143: 205–217.
