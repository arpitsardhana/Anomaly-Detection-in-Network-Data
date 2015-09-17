import os
import sys
import time
import csv
import matplotlib.pyplot as plt

input_file = str(sys.argv[1])


file_open = open(input_file,'r')

mul = 1
const = 1*60
list_time = list()
list_time.append(0);
count = 0
proto_dict = dict()
with open(input_file, 'rb') as f:
     for row in csv.reader(f, delimiter=',', skipinitialspace=True):
             #print '|'.join(row)
	     if row[1] == "Time" :
		continue
	    
             #print row[1]

             time = float(row[1])
	     proto = row[4]

	     if proto_dict.has_key(proto) :
		proto_dict[proto] += 1
	     else :
		proto_dict[proto] = 1

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
print str(proto_dict)
#fig = plt.figure()

#ax1 = fig.add_subplot(211)
#ax1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])
#ax2 = fig.add_subplot(212)
#ax2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])

#PLT.show()
#ax1.bar(range(len(proto_dict)), proto_dict.values(), align="center")
#ax1.set_xticks(range(len(proto_dict)), list(proto_dict.keys()),rotation = 90)
#ax1.set_xticks(range(len(proto_dict)), list(proto_dict.keys()))
#ax1.legend()
#ax1.set_xticks(xlabels_positions)
#ax1.set_xticklabels(xlabels, rotation=90)
#plt.show()
#ax2.plot(list_time)
#ax2.set_ylabel('Packets')
#ax2.set_xlabel('Time in hours division')
plt.plot(list_time)
plt.ylabel('Packets')
plt.xlabel('Time in hours division')

plt.show()


	
