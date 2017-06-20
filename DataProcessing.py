"""Aim1: To understand how the following 25 features are correlated with protein localization.
We are currently assigning weights 0,1 to each feature and applying SVM on the dataset"""

import os


#Creating a dictionary for modifications (row)

FeaturesArray=[]
i, Features= 0,dict()
for filename in os.listdir("CG/DataSets/Modifications"):  #looping over filenames or modification names
    if("_fixed.txt" in filename):
        Features[filename]=i   #Assigning feature files to a dictionary (numbers) for reference and matrix assignment
        FeaturesArray.append(filename)
        i=i+1

#Creating a dictionary for protein IDs(column) and sample labels    

ProteinIDArray=[]     
j, k, ProteinID, Samples=0,0, dict(), dict()     
root= "CG/DataSets/Localization info"
m= open("CG/DataSets/Labels.txt", 'w')
for filename in os.listdir(root):  #looping over filenames or modification names    
    if (".txt" in filename):
        f= open(os.path.join(root, filename), 'r')
        for line in f:
            if(line.rstrip() not in ProteinIDArray):
                ProteinID[line.rstrip()]= j
                ProteinIDArray.append(line.rstrip())
                Samples[line.rstrip()]=k   #0 is Golgi, 1 is lysosome
                v=str(Samples[line.rstrip()])
                m.write(v)
                m.write("\n")
                j=j+1
        k=k+1




dataMatrix = [[0 for x in range(len(ProteinIDArray))] for x in range(len(FeaturesArray))]

#Assigning dataMatrix the values
root= "CG/DataSets/Modifications"
for filename in os.listdir(root):
    if ("_fixed.txt" in filename):
        f= open(os.path.join(root, filename), 'r')
        for line in f:
            if(line.rstrip("\n") in ProteinID): dataMatrix[Features[filename]][ProteinID[line.rstrip("\n")]]=1
                  
    f.close()
        
for i in xrange(0, len(FeaturesArray)):
    s=0
    for j in xrange(0,len(ProteinIDArray)):
        s=s+ (dataMatrix[i][j])

    print s, FeaturesArray[i] 
            

A=[]
f= open("CG/DataSets/Modifications/O-linked_S_fixed.txt", 'r')
for line in f:
    if (line.strip() in ProteinIDArray):
        print "True"
    else:
        A.append(line.rstrip())


#write dataMatrix onto a file
h=open("CG/DataSets/DataMatrix.txt", 'w')
for row in xrange(len(FeaturesArray)):
    for col in xrange(len(ProteinIDArray)):
        value=str(dataMatrix[row][col]) +" "
        h.write(value)
    h.write("\n")

h.close()
m.close()

print Features    
    
#Proteins undergoing modifications
countGol=0
countLy=0
for x in ProteinIDArray:
    if(Samples[x]==0): countGol= countGol+1
    elif(Samples[x]==1): countLy=countLy+1
    
print countGol
print countLy
    
    
# combining/grouping features
dataMatrixCombo = [[0 for x in range(len(ProteinIDArray))] for x in range(len(FeaturesArray))]

FeaturesArrayCombo=[]
i, FeaturesCombo= 0,dict()
for filename in os.listdir("CG/DataSets/Modifications/Combo"):  #looping over filenames or modification names
    if("_combo.txt" in filename):
        FeaturesCombo[filename]=i   #Assigning feature files to a dictionary (numbers) for reference and matrix assignment
        FeaturesArrayCombo.append(filename)
        i=i+1

root= "CG/DataSets/Modifications/Combo"
for filename in os.listdir(root):
    if ("_combo.txt" in filename):
        f= open(os.path.join(root, filename), 'r')
        for line in f:
            if(line.rstrip("\n") in ProteinID): dataMatrix[FeaturesCombo[filename]][ProteinID[line.rstrip("\n")]]=1
                  
    f.close()

#write dataMatrixCombo onto a file
h=open("CG/DataSets/Modifications/Combo/DataMatrixCombo.txt", 'w')
for row in xrange(len(FeaturesArrayCombo)):
    for col in xrange(len(ProteinIDArray)):
        value=str(dataMatrix[row][col]) +" "
        h.write(value)
    h.write("\n")
print(len(FeaturesArrayCombo))

print(FeaturesArrayCombo)


