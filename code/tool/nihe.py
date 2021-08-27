'''
Author: your name
Date: 2021-03-31 22:25:50
LastEditTime: 2021-05-14 11:56:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\numpy\2.py
''' 
import matplotlib.pyplot as plt

import numpy as np

x = np.array([0.644,2.5,5.6,9.9,15.5])

y = np.array([25,100,225,400,625])

z1 = np.polyfit(x,y,1) 
p1= np.poly1d(z1)
#print(p1) #输出拟合的方程
yvals = p1(x)

plot1 = plt.plot(x,y,'*',label='original values')
plot2 = plt.plot(x,yvals,'r',label='polyfit values')
plt.xlabel('x^2')
plt.ylabel('Ix')
plt.legend(loc=4)  
plt.title('polyfitting')
print(p1)
plt.show()


