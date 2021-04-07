'''
Author: your name
Date: 2021-03-22 20:10:49
LastEditTime: 2021-03-24 20:34:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\matplotlib\zhe_xian_tu.py
'''
import matplotlib
from matplotlib import pyplot as plt
######该段为更新中文字体，具体使用查阅zh.md
from pylab import * 
import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 
mpl.rcParams['font.size'] = 9 
#######
#控制图像大小与清晰度
fig = plt.figure(figsize=(10,5),dpi=200) #dpi表示每英寸点个数
#传入数据
x = range(2,27,2)#数据在x轴的位置，需为一个可迭代对象
y = [15,13,14,5,17,20,25,26,26,24,22,18,25]
#控制x轴与y轴间隔
plt.xticks(x)#x要先定义
plt.yticks(range(5,30,1))#可以使用range
#输出
plt.plot(x,y) #生成图像
plt.savefig("./test.png") #可以保存为svg矢量图格式，放大不会有锯齿
#设置描述信息
plt.xlabel("时间")
plt.show()