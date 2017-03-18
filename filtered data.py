''''
final_data[0] means lat0
final_data[1] means lat1 and so on
'''
import csv
from collections import defaultdict

data_file = "as_mon_ws.txt"
no_of_coloums=28;
final_data=defaultdict(list)

with open(data_file,'r') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        for i in range(int(no_of_coloums)):
            if row[i] != 'NaN':
                final_data[i].append(float(row[i]))
                # print(row[i])
                pass
            pass

print("latitude 0 ")

print(final_data[0])
