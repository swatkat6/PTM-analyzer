import os

f= open("CG/DataSets/Miscellaneous/human_proteins (1).txt", 'r')
g= open("CG/DataSets/Modifications/LipidRaftAssociated.txt", "w")
f.readline()
for line in f:
    array=line.split()
    g.write(array[0]+"\n")
    
        
root= "CG/DataSets/Modifications"
for filename in os.listdir(root):
    if (".txt" in filename) and ("_fixed.txt" not in filename):
        temp=""
        f= open(os.path.join(root, filename), 'r')
        newfilename= filename.rstrip(".txt")+"_fixed.txt"
        g= open(os.path.join(root, newfilename), "w")
        array = f.readline().split()
        f.seek(0)
        if(len(array)>3):
            index=1
            for line in f:
                array=line.split()
                if((temp!=array[0]) and ("_HUMAN" in array[0])):
                    element=array[index]
                    g.write(element+"\n")
                    temp=array[0]    
        else:
            index=0
            for line in f:
                array=line.split()
                if((temp!=array[0]) and ("-" not in array[0])):
                    element=array[index]
                    g.write(element+"\n")
                    temp=array[0]      
        f.close()
        g.close()
