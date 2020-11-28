'''
Author: your name
Date: 2020-10-30 10:47:54
LastEditTime: 2020-10-31 17:07:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \mathmodel\study\LinearProgramming.py
'''
import numpy as np
from scipy.optimize import linprog
c = [1,-4]
A_ub = [[-3,1],[1,2]]
B_ub = [6,4]
x0_bounds = [None,None]
x1_bounds = [-3,None]
result = linprog(c,A_ub,B_ub,bounds = (x0_bounds,x1_bounds))
print(result) 