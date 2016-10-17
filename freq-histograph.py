# read data from file
import csv
import numpy as np
import matplotlib.pyplot as plt



data_file = "arabian_sea200602.pix"

#rowValue = input("Enter the row value")
rowValue = 4

result = []

with open(data_file,'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for row in reader:
        temp = float(row[rowValue])
        result.append(temp)


# sort the result data

sorted_data = sorted(result)

n = len(sorted_data)
plt.hist(sorted_data,bins=n,color="blue")
plt.title("histogram")  #enter ur title here
plt.xlabel("xlabe")
plt.ylabel("Frequency")

plt.show()
