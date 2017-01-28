'''
1. Make sure data file and code is in same pholder
2. 
'''

import csv

data_file = "as_mon_zonalmean_cnspfra.dat"
index=1

with open(data_file,'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for row in reader:  
       if float(row[0])>0:
        temp='row'+str(index)
        globals()[temp]=[round(float(x),2) for x in row if x != 'NaN']
        del globals()[temp][0] #commnet this line if you want include the 0th coloum
        index=index+1

#the list like row0,row1.....row27 will be created dynamically 
#number of lists created will depend on number of valid records

#Initial code that i wrote was more than 60 lines,it took more than 2hrs to reduce it to 14lines of code
