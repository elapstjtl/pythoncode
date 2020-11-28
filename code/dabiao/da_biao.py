'''
Author: your name
Date: 2020-10-27 19:25:35
LastEditTime: 2020-10-28 16:00:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\dabiao\da_biao.py
'''
def prime(i): # 判断素数，是返回1，不是返回0
    max = int(pow(i,0.5)+1)
    for m in range(2,max):
        if i % m == 0:
            return 0
    else:
        return 1



for i in range(2,100000000+1):
    if prime(i):
        i = str(i)
        if i == i[::-1]:
            print(i+',',end='')
print(' end')


