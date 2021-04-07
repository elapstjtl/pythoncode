'''
Author: your name
Date: 2021-03-31 22:25:50
LastEditTime: 2021-04-07 10:46:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\numpy\2.py
''' 
import matplotlib.pyplot as plt

import numpy as np

x = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,8,9,10,11])

y = np.array([0,15.33,20.86,25.21,29.20,32.91,36.28,39.52,42.54,45.44,48.27,50.95,53.52,56.00,58.35,62.90,67.32,71.30,75.20])

z1 = np.polyfit(x,y,5) #用3次多项式拟合  可以改为5 次多项式。。。。 返回三次多项式系数

p1= np.poly1d(z1)

print(p1) #在屏幕上打印拟合多项式

yvals = p1(x)#也可以使用yvals=np.polyval(z1,x)

plot1 = plt.plot(x,y,'*',label='original values')

plot2 = plt.plot(x,yvals,'r',label='polyfit values')

plt.xlabel('xaxis')

plt.ylabel('yaxis')

plt.legend(loc=4)  

plt.title('polyfitting')

plt.show()

plt.savefig('p1.png')