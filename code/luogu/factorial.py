'''
Author: your name
Date: 2020-10-26 09:59:28
LastEditTime: 2020-10-26 12:08:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\luogu\factorial.py
'''
def factorial(m):
    result = 1
    for i in range(1,m+1):
        result = result*i
    return result

n = eval(input())
end =1
result = 0
for i in range(1,n+1):
    result = factorial(i)+result
print(result)

