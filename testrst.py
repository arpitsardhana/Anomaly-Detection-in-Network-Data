import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc,rcParams
from pylab import *

print "Enter the file name"
#inp = raw_input()
inp = sys.argv[1]
f = open(inp,'r')

line = f.readlines()
minute = 60 

list_time = list() 
list_time.append(0);
count = 0
mul = 1
flag = 1

for i in range(0,1040):
	list_time.append(0)

for lines in line:
	#print lines[1]
	token = lines.split(',')
	#print token[1]
	time = float(token[1])
	count = int(time/60)
	list_time[count] += 1
	

b = sum(list_time)
print b
#del list_time[count]
#print str(list_time)
fontsize = 14
ax = gca()
plt.plot(list_time)


for tick in ax.xaxis.get_major_ticks():
     tick.label1.set_fontsize(fontsize)
     tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
     tick.label1.set_fontsize(fontsize)
     tick.label1.set_fontweight('bold')

xlabel('Time in per minute division', fontsize=16, fontweight='bold')
ylabel('Packets', fontsize=16, fontweight='bold')
legend()
plt.show()

