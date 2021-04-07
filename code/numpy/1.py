'''
Author: your name
Date: 2021-03-27 13:52:40
LastEditTime: 2021-04-07 11:22:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\numpy\1.py
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#绘制3D的图像
fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
x,y = np.meshgrid(x,y)
z = np.sin(np.sqrt(x **2 + y** 2))
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#压制到z平面上的等高线图
ax.contourf(x,y,z,zdir='z',offset = -2,cmap = 'rainbow')
ax.set_zlim(-2,2)

plt.show()