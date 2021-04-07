'''
Author: your name
Date: 2021-03-26 11:43:10
LastEditTime: 2021-03-26 11:44:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\matplotlib\practice\dawuzuoye.py
'''

import matplotlib
from matplotlib import pyplot as plt
######该段为更新中文字体，具体使用查阅zh.md
from pylab import *

matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 
mpl.rcParams['font.size'] = 9 
#######

x = range(1,11,1)
y = [0.032,0.088,0.039,0.015,0.138,0.190,0.387,0.265,0.285,0.646]

plt.plot(x,y)







plt.show()
