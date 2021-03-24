'''
Author: your name
Date: 2021-03-22 20:10:49
LastEditTime: 2021-03-22 20:40:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\matplotlib\zhe_xian_tu.py
'''
import matplotlib

from matplotlib import pyplot as plt
#控制图像大小与清晰度
fig = plt.figure(figsize=(20,10),dpi=600) #dpi表示每英寸点个数
#传入数据
x = range(2,27,2)#数据在x轴的位置，需为一个可迭代对象
y = [15,13,14,5,17,20,25,26,26,24,22,18,25]
#控制x轴与y轴
plt.xticks(x)#x要先定义
plt.yticks(range(5,30,1))#可以使用range
#输出
plt.plot(x,y) #生成图像
plt.savefig("./test.png") #可以保存为svg矢量图格式，放大不会有锯齿
plt.show()