'''
Author: your name
Date: 2021-04-29 19:55:45
LastEditTime: 2021-04-30 12:09:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\tool\temp.py
'''
import matplotlib.pyplot as plt
import math
import numpy as np

def average(a):
    sum = 0
    count = 0
    i = 0
    for i in range(0,len(a)):
        sum += a[i]
        count += 1
    average = sum / count
    print(" t1: average = %.2f"%(average))
    return average
t1 = [68.682,68.652,68.625,68.625,68.625]
t2 = [62.250,62.438,62.500,62.625,62.688]
avt1 = average(t1)
avt2 = average(t2)


x = np.array(list(range(140,381,20)))
y = np.array([64.875,64.5,64.125,63.812,63.438,63.125,62.814,62.438,62.125,61.812,61.5,61.125,60.812])
z1 = np.polyfit(x,y,1) 
p1= np.poly1d(z1)
print(p1) 
yvals = p1(x)

plot1 = plt.plot(x,y,'*',label='original values')
plot2 = plt.plot(x,yvals,'r',label='polyfit values')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.legend(loc=4)  
plt.title('polyfitting')
plt.show()

m = 693.4
c = 377
rp = 100.06/2
hp = 10.11
r = 99.47/2
h = 3.14
k = -0.01678
result = (m*c*h*k)/(math.pi*r*r*(avt1 - avt2)) *(2*hp + rp)/(2*hp + 2*rp)
print (result)