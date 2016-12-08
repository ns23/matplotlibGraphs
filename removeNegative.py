# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 19:57:18 2016
Removes negative values and rounds values to 2

@author: 
"""
import csv
#import numpy as np


data_file = "try.txt"
f2 = open('output1', 'w')


#rowValue = input("Enter the row value")
rowValue1 = 6
rowValue2 = 7

result = []

with open(data_file,'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for row in reader:
        if float(row[rowValue1]) >=0 and float(row[rowValue2]) >=0:
           row = filter(None, row) #this i used to remove extra space
           f2.write("\n")
           for item in row:
  				if '-'not in item and ':' not in item:
  					item = str(round(float(item),2)) /
  					f2.write("%s " % item)
  				else:
  					f2.write("%s " % item)
                
                     

f2.close()            
print "done"            