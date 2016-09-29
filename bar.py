#read data from file
import csv;
import numpy as np 
import matplotlib.pyplot as plt

data_file = "arabian_sea200602.pix"

result = {}

with open(data_file,'r') as f:
	reader = csv.reader(f,delimiter=' ')

	for row in reader:
		if row[0] in result:
			temp = float(row[4])
			result[row[0]].append(temp)
		else:
			result[row[0]] = [row[4]]


#Get all the keys of the list and store it in a tuple

keys = list(result.keys())
keys.sort()

#calculate mean and stanard devaition for the data

resultMean  =  []
resultStd	=  [] 	


for value in keys:
	temp = np.array(result[value],dtype="float")
	resultMean.append(np.mean(temp))
	resultStd.append(np.std(temp))



N = len(resultMean)
x = range(1,N+1)
width = 1/1.5

plt.title('Bar Graph')
plt.ylabel('total_AOD fine Mean', fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.bar(x, resultMean, width, color="blue")
plt.xticks(x,size="small")
plt.show()