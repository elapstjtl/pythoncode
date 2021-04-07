'''
Author: your name
Date: 2021-03-31 22:25:50
LastEditTime: 2021-04-07 21:41:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\numpy\2.py
''' 
import matplotlib.pyplot as plt

import numpy as np

x = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,8,9,10,11,12])

y = np.array([0,11.29,16.45,23.14,26.94,30.23,32.90,36.12,39.55,42.28,44.23,46.92,49.44,51.59,54.22,58.23,62.58,66.24,70.08,73.52])

z1 = np.polyfit(x,y,5) 
p1= np.poly1d(z1)
print(p1) 
yvals = p1(x)
m = y-yvals
np.savetxt('D:\pythoncode\code\Data\degree_of_uncertainty,csv',m,fmt='%f',delimiter=',')

plot1 = plt.plot(x,y,'*',label='original values')
plot2 = plt.plot(x,yvals,'r',label='polyfit values')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.legend(loc=4)  
plt.title('polyfitting')
# plt.show()

