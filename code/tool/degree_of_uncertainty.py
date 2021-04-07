'''
Author: your name
Date: 2021-03-19 12:06:47
LastEditTime: 2021-04-07 21:45:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\tool\degree_of_uncertainty.py
'''

import numpy as np

temp = 0
j=0
sum = sum2 = 0

a = np.loadtxt("D:\pythoncode\code\Data\degree_of_uncertainty,csv",delimiter=",")

for i in a:
    temp+=1
    sum += i
average = sum / temp #计算平均值

#计算A类不确定度
for j in range(0,temp):
    sum2 += (a[j]-average)*(a[j]-average)
ua = (sum2 / temp /(temp-1))**0.5
print("ua计算完成，请输入仪器误差")
#计算B类不确定度
temp = eval(input())
ub = temp / (3**0.5)
#计算标准不确定度
ux = (ua**2 + ub**2)**0.5
#相对不确定度
E = ux/average
#输出阶段
print(f"平均值={average}")
print(f"ua={ua}")
print(f"ub={ub}")
print(f"ux={ux}")
print(f"E={E}")


