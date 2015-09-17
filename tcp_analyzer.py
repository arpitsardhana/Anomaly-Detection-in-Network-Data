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
#proto_dict = dict()
tcp_dict = { 'SYN':0,'RST':0,'FIN':0 }
s = "SYN"
r = "RST"
a = "ACK"
fi = "FIN"
name = "RST.csv"
with open(input_file, 'rb') as f:
     for row in csv.reader(f, delimiter=',', skipinitialspace=True):
	     desc = row[len(row) -1 ]
	     desc.replace("[","")
	     desc.replace(",","")
	     #print desc
	     if desc.find(r) >= 0 :
		tcp_dict['RST']  += 1
             	with open(name,"ab") as myfile:
                	write = csv.writer(myfile,delimiter=',',quotechar='"')
                	write.writerow(row)

	     
	     if desc.find(s) >= 0 :
                tcp_dict['SYN'] += 1
             
	     if desc.find("FIN") >= 0 :
                tcp_dict['FIN'] += 1
	     

file_open.close()
	
print str(tcp_dict)

plt.bar(range(len(tcp_dict)), tcp_dict.values(), align="center")
plt.xticks(range(len(tcp_dict)), list(tcp_dict.keys()),rotation = 90)
plt.xticks(range(len(tcp_dict)), list(tcp_dict.keys()))
plt.legend()
plt.show()
plt.close()

	
