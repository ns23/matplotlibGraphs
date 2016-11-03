# read data from file
import csv
#import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def writeToFile(row6,row7,row8):
    thefile = open('data.txt', 'w')

    for i in range(0,len(row6)):
        thefile.write("%s %s %s" % (row6[i],row7[i],row8[i]))
    #print (item6,item7,item8



#rowValue = input("Enter the row value")
rowValue = [5,6,7,8]
row6=[]
row7=[]
row8=[]
result = []
i=0
data_file = "try" #replace with your file name
with open(data_file,'rU') as f:
    reader = csv.reader(f, delimiter=' ')

    for row in reader:
        print(i)
        i = i+1 
        fine = float(row[rowValue[1]])/float(row[rowValue[0]])
        #fine = fine
        row6.append(fine)
        #for row 7
        fine = float(row[rowValue[2]])/float(row[rowValue[0]])
        #fine = float(fine)
        row7.append(fine)
        #for row 8
        fine = float(row[rowValue[3]])/float(row[rowValue[0]])
        #fine = float(fine)
        row8.append(fine)
        

        
print(row8[0])       
sorted_data = sorted(row8)
count = Counter(sorted_data)


#call function to write to file
writeToFile(row6,row7,row8) # you can change name of the file if u want

n = len(sorted_data)
plt.hist(sorted_data,bins=500,histtype='step')
#plt.axis([0,1.1,0,400])
plt.title("Arabian Sea ")  #e11nter ur title here
plt.xlabel("fine fraction ")
plt.ylabel("Frequency")

plt.show()

print "done" 

#count of occurance of list items


