'''
Author: your name
Date: 2020-10-26 16:46:52
LastEditTime: 2020-10-26 17:12:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\luogu\count_number.py
'''
n,x = map(int,input().split())
x = str(x)
count= 0
a=[]
for i in range(1,n+1):
    a.append(str(i))
for i in range(0,n):
    for m in a[i]:
        for n in m:
            if n == x:
                count+=1
print(count)