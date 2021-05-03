'''
Author: your name
Date: 2021-04-13 10:58:07
LastEditTime: 2021-05-03 15:22:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\math\1.py
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

longxia = pd.read_excel(r"D:/pythoncode/math/data/longxia.xlsx",index_col = 0)
x = np.array(range(40,101,1))#长度计为x轴

y = np.array(list(longxia["weight"]))#y计为y轴，并对数据保留二位有效数字
for i in range(0,len(y)):
    y[i] = round(y[i],2)
 
z = np.polyfit(x,y,4)
p1 = np.poly1d(z)
print(p1)
y2 = p1(x)
plot1 = plt.plot(x,y)#作y的曲线
plot2 = plt.plot(x,y2) 

plt.legend()#图例表示

plt.xlabel("mm")#坐标轴意义
plt.ylabel("dg",rotation = 90)

plt.title("fig标题")#设置fig标题

plt.savefig("./1.png")#可以保存为svg矢量图格式，放大不会有锯齿
plt.show()
