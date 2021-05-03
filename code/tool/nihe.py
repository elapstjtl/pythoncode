'''
Author: your name
Date: 2021-03-31 22:25:50
LastEditTime: 2021-05-03 15:21:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\numpy\2.py
''' 
import matplotlib.pyplot as plt

import numpy as np

x = np.array([0.2,0.3,0.4,0.5,0.6,0.7,0.8])

y = np.array([0.16,0.32,0.48,0.63,0.80,0.95,1.01])

z1 = np.polyfit(x,y,5) 
p1= np.poly1d(z1)
#print(p1) #输出拟合的方程
yvals = p1(x)

plot1 = plt.plot(x,y,'*',label='original values')
plot2 = plt.plot(x,yvals,'r',label='polyfit values')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.legend(loc=4)  
plt.title('polyfitting')
plt.show()

