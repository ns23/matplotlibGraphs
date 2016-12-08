# read data from file
import csv
import numpy as np
import matplotlib.pyplot as plt
import collections
from collections import Counter
import csv


data_file = "arabian_sea200602.pix"

#rowValue = input("Enter the row value")
rowValue = 4

result = []

with open(data_file,'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for row in reader:
        temp = float(row[rowValue])
        result.append(temp)

# Get all the keys of the list and store it in a tuple
newData = Counter(result)


# make the data  ordered
od = collections.OrderedDict(sorted(newData.items()))



keys = list(newData.keys())


# calculate mean and stanard devaition for the data

