'''
Author: your name
Date: 2020-10-25 16:31:37
LastEditTime: 2020-10-25 16:49:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\luogu\number_zhijiao_sanjiaoxing.py
'''
n = int(input())
n1 = n
count=1
for i in range(0,n):
    for j in range(0,n1):
        print('{:0>2}'.format(count),end = '')
        count +=1
    else:
        print()
        n1 = n1-1
