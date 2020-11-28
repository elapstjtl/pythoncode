'''
Author: your name
Date: 2020-10-23 10:52:00
LastEditTime: 2020-11-22 22:56:19
LastEditors: your name
Description: In User Settings Edit
FilePath: \pythoncode\python\test\test.py
'''
def gys (n1,n2):
    min = n1
    if n1>n2:
        min = n2
    for i in range(min,1,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i

n1 = eval(input())
n2 = eval(input())
result = gys(n1,n2)
print(result)

