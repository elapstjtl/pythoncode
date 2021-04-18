'''
Author: your name
Date: 2021-04-18 12:32:03
LastEditTime: 2021-04-18 12:35:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\tool\LP.py
'''
from scipy import optimize
import numpy as np

c = np.array([])
A = np.array([])
b = np.array([])
Aeq = np.array([])
beq = np.array([])
res = optimize.linprog(c,A,b,Aeq,beq)
print(res)