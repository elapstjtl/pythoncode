'''
Author: your name
Date: 2021-03-24 20:40:19
LastEditTime: 2021-03-25 22:43:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\matplotlib\practice\1.py
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
y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

plt.plot(x,y_1,label="自己")#作y_1的曲线
plt.plot(x,y_2,label="同桌")
plt.legend()#图例表示
xticklabels = ["{}岁".format(i) for i in x] #设置每个坐标的名字
yticklabels = ["{}个".format(i) for i in range(0,7,1)]

plt.xticks(x,xticklabels,rotation=90)#使名字对应坐标轴上的点
plt.yticks(range(0,7,1), yticklabels)

plt.xlabel("年龄")#坐标轴意义
plt.ylabel("女友数量")

plt.title("fig标题")#设置fig标题

plt.savefig("./1.png")#可以保存为svg矢量图格式，放大不会有锯齿
plt.show()
