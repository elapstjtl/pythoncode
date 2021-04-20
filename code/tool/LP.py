'''
Author: your name
Date: 2021-04-18 12:32:03
LastEditTime: 2021-04-18 14:22:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\tool\LP.py
'''
from scipy import optimize
import numpy as np

c = np.array([])#目标函数
A = np.array([[])#不等式左式，二维数组
b = np.array([])#不等式右式，一维
Aeq = np.array([[]])#等式左式，二维数组
beq = np.array([])#等式右式，一维

res = optimize.linprog(-c,A,b,Aeq,beq)#解
print(res) 