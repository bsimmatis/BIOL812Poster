import pandas as pd
import numpy as np

#Accessing data
Jackfish=pd.ExcelFile('./Jackfish NIRS_June28.xls')
Muskrat=pd.ExcelFile('./Muskrat2017_1A_FullSpectra.xls')
L06133=pd.ExcelFile('./06 133 NIRS.xls')
L06137=pd.ExcelFile('./06 137 NIRS new2.xlsx')
L08160=pd.ExcelFile('./08 160 NIRS new2.xlsx')

#Defining sheets
sheets_JF=Jackfish.sheet_names
sheets_MR=Muskrat.sheet_names
sheets_L06133=L06133.sheet_names
sheets_L06137=L06137.sheet_names
sheets_L08160=L08160.sheet_names

#Defining sheetnames
sheetNames_JF=[u'Spectra', u'Sheet1', u'Analog']   
sheetNames_MR=[u'Spectra', u'Analog', u'Inf Chl a']  
sheetNames_L06133=[u'Inf Chl a', u'Spectra', u'Analog', u'650 to 700 nm']  
sheetNames_L06137=[u'Spectra', u'Sheet1', u'Inf Chl a']  
sheetNames_L08160=[u'Spectra', u'Sheet1', u'Analog']  
    
#Parsing. Focusing on Chl.a ranges right now i.e. only 1 sheet
jf_sheet1=Jackfish.parse("Sheet1")
mr_sheet1=Muskrat.parse("Inf Chl a")
L06133_sheet1=L06133.parse("Inf Chl a")
L06137_sheet1=L06137.parse("Sheet1")
L08160_sheet1=L08160.parse("Sheet1")

#Importing handy stuff with handy short-forms
import matplotlib as mp
from random import *
from random import shuffle

#Getting columns from sheets responsible for depth (cm) of sample slices
jf_sheet1_header=jf_sheet1.columns.values
mr_sheet1_header=mr_sheet1.columns.values
L06133_sheet1_header=L06133_sheet1.columns.values
L06137_sheet1_header=L06137_sheet1.columns.values
L08160_sheet1_header=L08160_sheet1.columns.values

#Getting depth information for all lakes. dc='depth column'
dc_jf=np.where(jf_sheet1_header=='Depth')[0]
depth_jf=jf_sheet1.iloc[:,dc_jf[0]]
#
dc_mr=np.where(mr_sheet1_header=='Depth (cm)')[0]
depth_mr=mr_sheet1.iloc[:,dc_mr[0]]
#
dc_L06133=np.where(L06133_sheet1_header=='Sample')[0]
depth_L06133=L06133_sheet1.iloc[:,dc_L06133[0]]
#
dc_L06137=np.where(L06137_sheet1_header=='Depth')[0]
depth_L06137=L06137_sheet1.iloc[:,dc_L06137[0]]
#
dc_L08160=np.where(L08160_sheet1_header=='DEPTH (cm)')[0]
depth_L08160=L08160_sheet1.iloc[:,dc_L08160[0]]

allDepths=[depth_mr, depth_L06133, depth_L06137, depth_L08160]

#Define logical comparisons for detecting int, str, float. Useful later
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# 
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
#    
def is_str(s):
    try:
        str(s)
        return True
    except ValueError:
        return False
#
#Define a script to identify the absorbances in the inputs. Half of the column headers are strings (!!!)
#dat_header is a header input, dat is an input dataframe
def trim(dat_header, dat): 
    #Counter
    iNd=0
    for v in dat_header:
        #Check if header entry is_str. The False in the exception case was a wild guess that actually worked and is robust
        if is_str(v)==True:
            try:
                int(v)
                dat_header[iNd]=int(v)
            except ValueError:
                False
        #Increment counter
        iNd+=1  
    #Pre-allocate null array of indices    
    headerInds=np.zeros((len(dat_header),1),dtype=int)   
    
    #Identify all header values that are dtype=int with a '1'  
    for u in np.arange(0,len(dat_header)):
        if type(dat_header[u])==int:
            headerInds[u]=1

    #Transpose. I'm a visual person and I like seeing column indices as a row vector
    np.transpose(headerInds)
    
    #"Numeric absorbance" (num_abs) values. Identified as dataset columns with int titles (i.e. are abs. values)
    num_abs=dat.iloc[:, headerInds[:,0]==1]
    return num_abs
#Tidying up the columns from the DATES files to remove NaNs and strs
def trim_header(dat_header):
    iNd=0
    i2del=[]
    i2keep=[]
    for v in dat_header:
        #Check if header entry is_str. The False in the exception case was a wild guess that actually worked and is robust
        if is_str(v)==True:
            try:
                float(v)
                dat_header[iNd]=float(v)
                
                if np.isnan(v)==False:
                    i2keep.append(int(iNd))
            except ValueError:
                i2del.append(int(iNd)) #A dummy array to keep the code running happily. It works this way, best not to perturb it 
        #Increment counter
        iNd+=1  
    i2keep=np.asarray(i2keep)
    dat_header_trimmed=[]
    for vt in i2keep:   
        dat_header_trimmed.append(dat_header[vt])
    return dat_header_trimmed
#
jf_data=pd.DataFrame(trim(jf_sheet1_header, jf_sheet1))  
mr_data=pd.DataFrame(trim(mr_sheet1_header, mr_sheet1)) 
L06133_data=pd.DataFrame(trim(L06133_sheet1_header, L06133_sheet1)) 
L06137_data=pd.DataFrame(trim(L06137_sheet1_header, L06137_sheet1)) 
L08160_data=pd.DataFrame(trim(L08160_sheet1_header, L08160_sheet1))  
allData=[mr_data, L06133_data, L06137_data, L08160_data]

#Accessing data for ages of sediment samples. This is as above for absorbances
#Jackfish_dates=pd.ExcelFile('./Jackfish NIRS_June28.xls')
Muskrat_dates=pd.ExcelFile('./Muskrat 1A Dates.xlsx')
L06133_dates=pd.ExcelFile('./06-133 Dates.xlsx')
L06137_dates=pd.ExcelFile('./06-137 Dates.xlsx')
L08160_dates=pd.ExcelFile('./08-160 Dates new.xlsx')

#Defining sheets
#sheets_JF_dates=Jackfish_dates.sheet_names
sheets_MR_dates=Muskrat_dates.sheet_names
sheets_L06133_dates=L06133_dates.sheet_names
sheets_L06137_dates=L06137_dates.sheet_names
sheets_L08160_dates=L08160_dates.sheet_names

#Defining sheetnames
#sheetNames_JF_dates=[u'Spectra', u'Sheet1', u'Analog']   
sheetNames_MR_dates=[u'Muskrat 1A Dates']  
sheetNames_L06133_dates=[u'06-133 Dates']  
sheetNames_L06137_dates=[u'06-137 Dates']  
sheetNames_L08160_dates=[u'08-160 Dates']  
    
#Parsing
#jf_sheet1=Jackfish_dates.parse("Sheet1")
mr_dates=Muskrat_dates.parse("Muskrat 1A Dates")
L06133_dates=L06133_dates.parse("06-133 Dates")
L06137_dates=L06137_dates.parse("06-137 Dates")
L08160_dates=L08160_dates.parse("08-160 Dates")        
allDates=[mr_dates, L06133_dates, L06137_dates, L08160_dates]

#Pulling out the columns corresponding to the ages. PARAMETERIZE
mr_dates_col=list(mr_dates.iloc[:, 1])
L06133_dates_col=list(L06133_dates.iloc[:, 1])
L06137_dates_col=list(L06137_dates.iloc[:, 1])
L08160_dates_col=list(L08160_dates.iloc[:, 1])
allDatesCol=[mr_dates_col, L06133_dates_col, L06137_dates_col, L08160_dates_col]

#Defining the arrays of sediment sample ages
ages_mr=trim_header(mr_dates_col)
ages_L06133=trim_header(L06133_dates_col)
ages_L06137=trim_header(L06137_dates_col)
ages_L08160=trim_header(L08160_dates_col)
allAges=[ages_mr, ages_L06133, ages_L06137, ages_L08160]

#This can be user-defined. It requires knowledge of the dating results
#Below, the target dates are identified based on the closest values available
#in the date files. The corresponding sample depths are found, and the 
#rows that relate to these depths in the absorbance data are isolated
tgtYrs=[10,30,50,70]
tgtYrsLbl=[str(ty) for ty in tgtYrs]

#More user-definable variables. Select KFUNC to use the corresponding kernel.
#Cost is a penalty for misclassification. C=4 is a sweet spot.
#z0Max is used for controlling the number of repetitions in the z0 loop below. Read on
#FYI the SVM part is about 60 lines away. Patience, not there yet
kernels=['linear', 'poly', 'rbf', 'sigmoid']
kfunc=3
Cost=4
z0Max=100

#Lakechoices allow the user to select lakes to analyse
lakeChoice1=2
lakeChoice2=3

#Grabbing more data. Getting array shape for later calculations
datesData=[allDates[lakeChoice1], allDates[lakeChoice2]]
depthData=[allDepths[lakeChoice1], allDepths[lakeChoice2]]
lake_data2=[allData[lakeChoice1], allData[lakeChoice2]]
ageData=[allAges[lakeChoice1], allAges[lakeChoice2]]
dim_L=np.shape(allData[lakeChoice1])

iNd=0 #A counter
dated_data_array=np.zeros([len(tgtYrs),dim_L[1],len(ageData)])

for va in ageData:
    iNd2=0 #Another counter

    for vb in tgtYrs:
        #Finding a vector of differences between the target age(s) and the available sample ages
        diffs=np.asarray(va)-vb 
        diffs=list(np.abs(diffs))
        #Find the min of the absolute diffs. i.e. the closest sample age to the target age
        closest=va[diffs.index(min(diffs))] 
        ageCRS=list(datesData[iNd]["Age (CRS)"])
        depthCM=list(datesData[iNd]["Midpoint Depth"])
        #Grab the depth that corresponds to each target age from each sample set
        targetRowDepth=depthCM[ageCRS.index(closest)] 
        depthData[iNd]=list(depthData[iNd])
        year_data=lake_data2[iNd].iloc[depthData[iNd].index(targetRowDepth),:]
        year_data=np.matrix(year_data)
        #year_data=np.transpose(year_data)
        dated_data_array[iNd2, :, iNd]=year_data
        iNd2+=1 #Increment counters!
    iNd+=1
        
#Throw all of the data into a list. This allows flexibility and a parameterized script
lake_data=[np.transpose(dated_data_array[:,:,0]), np.transpose(dated_data_array[:,:,1])]
#lake_data=[jf_data, mr_data, L06133_data, L06137_data, L08160_data] 
#The above line is available to be commented back in. Wouldn't recommend, might break the code
allLakeNames=['Muskrat Lake', 'Lake 06-133', 'Lake 06-137', 'Lake 08-160']
lake_names=[allLakeNames[lakeChoice1], allLakeNames[lakeChoice2]]
#lake_names=['Jackfish Lake', 'Muskrat Lake', 'Lake 06-133', 'Lake 06-137', 'Lake 08-160']
#Same as above. Could comment the previous line in, 10/10 wouldn't recommend.

#Dims is for reference when looking at the variable explorer window in Spyder3, to see what I'm working with. A diagnostic aid
dims=[np.shape(lake_data[0])[0], np.shape(lake_data[1])[0]]
#dims=[np.shape(lake_data[0])[0], np.shape(lake_data[1])[0], np.shape(lake_data[2])[0], np.shape(lake_data[3])[0], np.shape(lake_data[4])[0]]

capturedParamArray=np.zeros((z0Max, len(tgtYrs)), dtype=int)
#In the event that multiple simulations are not needed,
#comment out the z0 loop and de-comment the z1 and z2 loops
#Also comment out the z1=0 and z2=1 bits. These control the lakes
#that are chosen out of the available pool.
for z0 in np.arange(0,z0Max):  
    print('Starting outer loop', z0)    
    #for z1 in np.arange(0,len(lake_data)):
    #    
    #    #Event codes
    #    print('Starting outer loop ', z1)
    #    
    #    for z2 in np.arange(0,len(lake_data)):
    #
    #        #More event codes
    #        print('Inner loop ', z2)
    
    #Selecting lakes to use in analyses from the above list
    z1=0
    z2=1
    Lake1=lake_data[z1]
    Lake2=lake_data[z2]
    
    dim_L1=np.shape(Lake1)
    dim_L2=np.shape(Lake2)
            
    #Defining batches and initializing arrays for SVM training, further below
    batches=9
    batchSize=(dim_L1[0]+dim_L2[0])//batches #The floor division operator is //
    varWiseAcc2=[]
    varWiseAcc2_SD=[]
    meanAcc2=[]
    #pToUse=np.linspace(0,(dim_L1[0]+dim_L2[0]),(dim_L1[0]+dim_L2[0])+1, dtype=int) #Make sure to pay attention to this one
    pToUse=np.linspace(0,len(tgtYrs)-1,len(tgtYrs), dtype=int)
    paramArray=[]
    paramArray=np.array(paramArray, dtype=int)
    
    #This loop controls how many items are built into each model
    for t in np.linspace(0,len(tgtYrs)-1,len(tgtYrs), dtype=int):
        varWiseAcc=[]
        varWiseAcc_SD=[]
        iNd=0
        #This loop is responsible for controlling the number of variables to try at each position
        #in the model. The number in the pool of available ones decrements with each run-through
        for k in np.linspace(1,len(pToUse),len(pToUse), dtype=int): 
            #Initializing arrays that will be cleared each time the loop runs.
            #Values are captured further below for analysis
            finalAcc=[]
            meanAcc1=[]
            
            #Even more event codes
            print('Trying variable', k)
            for j in np.arange(1,100):
                
                #Generate random array to scramble data
                matSize=dim_L1[0]+dim_L2[0]
                scramble=list(range(0,matSize))
                shuffle(scramble)
                scramble=np.asarray(scramble)
                
                #Concatenating data together
                X=np.concatenate((Lake1,Lake2), axis=0);
                y=[True]*dim_L1[0]+[False]*dim_L2[0] #y is of type 1D LIST 
                
                #Re-formatting the data matrix 'X'
                X=np.asarray(X)
                #X=np.transpose(X) #It seems that the size of the LABELS array has to be equivalent to the FIRST DIM of X
            
                #Scramble the data and labels 
                X=X[scramble, :]
        
                #Build the array that will be used for training/testing
                if t==0:
                    X=X[:, 0]
                elif t>0:
                    X[:, np.append(paramArray,k-1)]
                    
                y0=[y[sc] for sc in scramble]
                numTrue=np.sum(y0)
                numFalse=len(y0)-np.sum(y0)
                
                z=1 #Counter variable that controls the intervals used in each batch
                
                for i in range(0,batches-1):
                    #Cryptically-named arrays that define the start/stop points of each batch
                    start=[]
                    stop=[]
                    
                    #Select test-sets (X and y). Will be reomved later from main dataset. 
                    #This is the most efficient way to do this in my experience
                    #Could probably also be done with data.frames and $ubsets
                    if t==0:
                        X_test=X[(z-1)*batchSize:z*batchSize]
                    elif t>0:
                        X_test=X[(z-1)*batchSize:z*batchSize, :]
                        
                    y_test=y0[(z-1)*batchSize:z*batchSize]
                    
                    #Define batch start/stop points
                    start=(z-1)*batchSize
                    stop=z*batchSize
                    
                    #Remove test-set data from the training-set
                    rows2remove=np.arange(start, stop, 1, dtype=int)
                    X_train=np.delete(X, rows2remove, 0)
                    y_train=np.delete(y, rows2remove)
                    
                    
                    if t==0:
                        X_train=X_train.reshape(-1,1) #This reshape is necessary to make the SVM accept an Nx1 vector as input
                        X_test=X_test.reshape(-1,1)
                    elif t>0:
                        X_train=X_train #To satisfy the silly IF/ELIF statement
                        X_test=X_test
                    
                    #Get started with SVM using the training set
                    from sklearn import svm
                    clf = svm.SVC(kernel=kernels[kfunc], C=Cost, class_weight='balanced') #Instantiate an SVM classifier. RBF is the default "I dunno what's going to happen" kernel
                    clf.fit(X_train, y_train)
                    
                    #Predict using the test set
                    estLabels=clf.predict(X_test)
                    matches=estLabels==y_test
                    
                    #Determine classification accuracy
                    accuracy=100*np.sum(matches)/len(y_test)
                    accuracy=accuracy.round(2)
                    finalAcc.append(accuracy)
                    
                    #Clear a pile of variables. To avoid accidental inclusion of data from previous loop iterations
                    del accuracy 
                    del X_train 
                    del y_train 
                    del X_test 
                    del y_test
                    
                    #Increment batch counter
                    z+=1
                
                #Calculate batch-wise accuracy
                meanAcc1.append(np.mean(finalAcc))
                
            #Calculate accuracy across all batches, averaged over n-iterations (increased precision of estimate)
            meanAcc2=np.mean(meanAcc1)
            varWiseAcc.append(np.mean(meanAcc2))
            varWiseAcc_SD.append(np.std(meanAcc1))
            
            #Get the highest-accuracy variable, remove it from the pool of available ones, to incrementally build a more accurate model
        found=varWiseAcc.index(max(varWiseAcc))
        
        #When will the event codes stop?!
        print(varWiseAcc)
        print(varWiseAcc_SD)
        print(found)
        varWiseAcc2.append(max(varWiseAcc))
        varWiseAcc2_SD.append(varWiseAcc_SD[found])
        paramArray=np.append(paramArray, int(pToUse[found]))
        pToUse=np.delete(pToUse, found)
    capturedParamArray[z0,:]=paramArray
    print(capturedParamArray)    
        
    #Setting coordinates for a shaded +/-1SD patch
    xvals=np.linspace(0,len(tgtYrs)-1,len(tgtYrs))
    xvals=xvals.reshape(-1,1)
    yvals1=np.asarray(varWiseAcc2)-np.asarray(varWiseAcc2_SD)
    yvals2=np.asarray(varWiseAcc2)+np.asarray(varWiseAcc2_SD)
    yvals1=yvals1.reshape(-1,1)
    yvals2=yvals2.reshape(-1,1)
    polyCoords=np.concatenate((np.concatenate((xvals, np.flipud(xvals)), axis=0), np.concatenate((yvals1, np.flipud(yvals2)), axis=0)), axis=1)
    
    #Defining the tick labels for the plot in terms of useful age markers
    ageLbl=[tgtYrsLbl[lb] for lb in paramArray] 
    
    #Plot the whole shebang. Taking breaks in between to generate figures
    #These are accuracy plots with a +/-1SD boundary patch
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpp
    plt.ion()
    plt.show()
    fig1=plt.figure()
    titleSTR='SVM accuracy (%s vs %s), %s kernel' %(lake_names[z1], lake_names[z2], kernels[kfunc])
    plt.title(titleSTR)
    ax1=fig1.add_subplot(111)
    patch1=mpp.Polygon(polyCoords, closed=True, alpha=0.2, fc='red', ec='black')
    ax1.add_patch(patch1)
    ax1.plot(varWiseAcc2, color='blue', linewidth=2)
    plt.xlim([0,len(tgtYrs)-1])
    plt.ylim([30,80])
    plt.xticks(np.linspace(0,len(tgtYrs)-1,len(tgtYrs)), ageLbl)
    ax1.set_ylabel('Accuracy (%)')
    ax1.set_xlabel("Sediment age at collection (years)")
    plt.draw()
    plt.pause(1)

#Determining and plotting the most frequent appearances at each position in the models. 
#Have to run the simulations 100x or so to get this accurate (z0 loop and related parameters)
from scipy import stats
modeVals=stats.mode(capturedParamArray)
modes=modeVals[0]
props=modeVals[1]
modes=modes[0].reshape(1,-1)
props=props[0].reshape(1,-1)

#Getting modes at each of the N positions
modeData=np.concatenate((modes, props), axis=0)
modeData.sort(axis=1)
ageLbl2=[tgtYrsLbl[lb] for lb in modeData[0, :]] 

#Plotting
plt.ion()
plt.show()
fig1=plt.figure()
titleSTR='Modal selection position of variables'
plt.title(titleSTR)
ax1=fig1.add_subplot(111)
ax1.plot(np.linspace(0,3,4), modeData[1, :], color='blue', linewidth=2, marker='o')
plt.xlim([0,len(tgtYrs)-1])
plt.ylim([25,40])
plt.xticks(np.linspace(0,len(tgtYrs)-1,len(tgtYrs)), ageLbl2)
ax1.set_ylabel('Models included in (%)')
ax1.set_xlabel("Sediment age (years)")
plt.draw()
plt.pause(1)


#Determining and plotting the appearance of variables within the first 2 positions of the model during the iterative
#model-building process
freq=np.zeros((1, len(modeData[1, :])), dtype=int)
for i in np.linspace(0,len(modeData[0, :])-1,len(modeData[0, :]), dtype=int):
    freq[0][i]=len(np.where(np.concatenate((capturedParamArray[:,0], capturedParamArray[:,1]))==i)[0])
    
plt.ion()
plt.show()
fig1=plt.figure()
titleSTR='Modal selection position of variables'
plt.title(titleSTR)
ax1=fig1.add_subplot(111)
ax1.plot(np.linspace(0,3,4), freq[0], color='blue', linewidth=2, marker='o')
plt.xlim([0,len(tgtYrs)-1])
plt.ylim([40,60])
plt.xticks(np.linspace(0,len(tgtYrs)-1,len(tgtYrs)), ageLbl2)
ax1.set_ylabel('Models included in (%)')
ax1.set_xlabel("Sediment age (years)")
plt.draw()
plt.pause(1)

















