'''
Author: your name
Date: 2021-05-03 16:00:03
LastEditTime: 2021-05-04 15:08:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\math\homework\long_xia_yang_zhi\1.py
'''
import pandas as pd
import numpy as np
from sympy import *
from sympy import init_printing
import matplotlib
from matplotlib import pyplot as plt
######该段为更新中文字体，具体使用查阅zh.md
from pylab import *

matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 
mpl.rcParams['font.size'] = 9 
#######



dierate = 0.8
btnum3 = 1.109 * 10000
btnum2 = btnum3 *0.5
year = list(range(1,21,1))
longnum = [3.8,3.93,3.96,4.03,4.11,4.14,4.17,4.18,4.27,4.4,4.59,4.84,4.99,5.08,5.18,5.31,5.4,5.47,5.54,5.61]

x = np.array(year) 
y = np.array(longnum)

z1 = np.polyfit(x,y,4) 
p1= np.poly1d(z1)
print(p1) #输出拟合的方程
yvals = p1(x)
ansx = list(range(21,31,1))
for i in ansx:
    print(p1(i))

# plot1 = plt.plot(x,y,'*',label='原数据')
# plot2 = plt.plot(x,yvals,'r',label='拟合曲线')
# plt.xlabel('年份')
# plt.ylabel('龙虾只数/千只')
# plt.legend(loc=4)  
# plt.title('小龙虾只数关于时间拟合曲线')
# plt.show()