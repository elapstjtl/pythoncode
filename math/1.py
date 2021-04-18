'''
Author: your name
Date: 2021-04-13 10:58:07
LastEditTime: 2021-04-13 19:30:34
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

xin_price = pd.read_excel(r"math\data\xin.xlsx",usecols=[2])#房屋价格
x = xin_price.index.tolist() #x轴为编号
y = xin_price['价格'].values.tolist()#y轴为房屋价格
#处理价格中售价待定的数据
for i in range(0,len(y)-1):
    if y[i] == "售价待定":
        y[i] = 0
    else:
        y[i] = int(y[i])

