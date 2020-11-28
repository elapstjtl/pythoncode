'''
Author: your name
Date: 2020-11-08 10:19:22
LastEditTime: 2020-11-08 14:47:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\math\test.py
'''
import math
pi = math.pi
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(1,7,1000)
s = (-0.5*pi-2)*r**2 + 15*r   #`s关于r的函数`
plt.plot(r,s,'r',linewidth = 2)
plt.show()