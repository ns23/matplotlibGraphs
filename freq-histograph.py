# read data from file
import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


data_file = "arabian_sea200602.pix"

#rowValue = input("Enter the row value")
rowValue = 5

result = []

with open(data_file,'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for row in reader:
        if row[rowValue] == '-999.000000':
            continue

        temp = float(row[rowValue])
        result.append(temp)


#count of occurance of list items
occurance_count = Counter(result)

# sort the result data
sorted_data = sorted(result)

n = len(sorted_data)
plt.hist(sorted_data,bins=n,color="blue",range=[0,1])
plt.title("histogram")  #enter ur title here
plt.xlabel("xlabe")
plt.ylabel("Frequency")
plt.show()
