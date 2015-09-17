import os
import sys
import time
import csv
import matplotlib.pyplot as plt
import operator
from pylab import *

input_file = str(sys.argv[1])


file_open = open(input_file,'r')

mul = 1
const = 1*60
list_time = list()
list_time.append(0);
count = 0
source_ip = { }
dest_ip = { }
source_port = { }
dest_port = { }

with open(input_file, 'rb') as f:
     for row in csv.reader(f, delimiter=',', skipinitialspace=True):
            
	     if row[1] == "Time" :
		continue
	     src = row[2]
	     dst = row[3]
	     token = row[len(row) - 1].split()
	     src_p = token[0]
	     dst_p = token[2]	    
	     if source_ip.has_key(src) :
		source_ip[src] += 1
	     else :
		source_ip[src] = 1
		
	     if dest_ip.has_key(dst) :
                dest_ip[dst] += 1
             else :
                dest_ip[dst] = 1

             if source_port.has_key(src_p) :
                source_port[src_p] += 1
             else :
                source_port[src_p] = 1

             if dest_port.has_key(dst_p) :
                dest_port[dst_p] += 1
             else :
                dest_port[dst_p] = 1
file_open.close()
#print str(source_ip)
#print str(dest_ip)
#print str(source_port)
#print str(dest_port)
total_src_ports = 0
total_dst_ports = 0
source_port_s = source_port.copy() 
dest_port_s = dest_port.copy() 
count = 0
for key,value in source_port.iteritems():
	total_src_ports += value
	if value < 50:
		del source_port_s[key]

count = 0
for key,value in dest_port.iteritems():
	total_dst_ports += value
	if value < 70:
		del dest_port_s[key]

print len(dest_port)
print len(source_port)
print total_src_ports
print total_dst_ports


	
#plt.bar(range(len(source_ip)), source_ip.values(), align="center")
#plt.xticks(range(len(source_ip)), list(source_ip.keys()),rotation = 90)
#plt.ylabel("source ip vs Packets")
#plt.xlabel("Source_ip")
#plt.show()
#plt.bar(range(len(dest_ip)), dest_ip.values(), align="center")
#plt.xticks(range(len(dest_ip)), list(dest_ip.keys()),rotation = 90)
#plt.ylabel("Dest ip vs Packets")
#plt.xlabel("Dest_ip")
#plt.show()
fontsize = 16
ax = gca()
plt.plot(list_time)

#plt.gca().tight_layout()
plt.gcf().subplots_adjust(bottom=0.15)
for tick in ax.xaxis.get_major_ticks():
     tick.label1.set_fontsize(fontsize)
     tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
     tick.label1.set_fontsize(fontsize)
     tick.label1.set_fontweight('bold') 
      
#xlabel('Time in per minute division', fontsize=16, fontweight='bold')
#ylabel('Packets', fontsize=16, fontweight='bold')  
legend()
#plt.show()

plt.bar(range(len(source_port_s)), source_port_s.values(), align="center")
plt.xticks(range(len(source_port_s)), list(source_port_s.keys()),rotation = 90)
plt.ylabel("source port vs Packets", fontsize=16, fontweight='bold')
plt.xlabel("Source_port", fontsize=16, fontweight='bold')
plt.show()
plt.bar(range(len(dest_port_s)), dest_port_s.values(), align="center")
plt.xticks(range(len(dest_port_s)), list(dest_port_s.keys()),rotation = 90)
plt.ylabel("Dest  port vs Packets",fontsize=16, fontweight='bold')
plt.xlabel("Dest_port", fontsize=16, fontweight='bold')
plt.show()
plt.bar(range(len(source_ip)), source_ip.values(), align="center")
plt.xticks(range(len(source_ip)), list(source_ip.keys()),rotation = 90)
plt.ylabel("source ip vs Packets",fontsize=16, fontweight='bold')
plt.xlabel("Source_ip",fontsize=16, fontweight='bold')
plt.show()
plt.bar(range(len(dest_ip)), dest_ip.values(), align="center")
plt.xticks(range(len(dest_ip)), list(dest_ip.keys()),rotation = 90)
plt.ylabel("Dest ip vs Packets",fontsize=16, fontweight='bold')
plt.xlabel("Dest_ip",fontsize=16, fontweight='bold')
plt.show()

