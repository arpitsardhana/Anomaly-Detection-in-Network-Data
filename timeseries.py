import os
import sys
import time
import csv
import matplotlib.pyplot as plt

input_file = str(sys.argv[1])


file_open = open(input_file,'r')

mul = 1
const = 60*60
list_time = list()
list_time.append(0);
count = 0

with open(input_file, 'rb') as f:
     for row in csv.reader(f, delimiter=',', skipinitialspace=True):
             #print '|'.join(row)
	     if row[1] == "Time" :
		continue
	    
             #print row[1]

             time = float(row[1])
             if time < mul*const :
                list_time[count] += 1
             else:
                list_time.append(1)
                mul += 1
		count += 1

file_open.close()
#print  ",".join(str(list_time))
sum_total = 0
for item in list_time:
	print str(item)
	sum_total = sum_total + item
	
print str(sum_total)
plt.plot(list_time)
plt.ylabel('Packets')
plt.xlabel('Time in hours division')
plt.show()


	
