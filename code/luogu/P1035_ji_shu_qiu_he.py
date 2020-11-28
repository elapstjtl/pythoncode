'''
Author: your name
Date: 2020-10-26 18:08:11
LastEditTime: 2020-10-26 18:10:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\luogu\P1035_ji_shu_qiu_he.py
'''
k = eval(input())
sum = 0
n=0
while(sum<=k):
    n+=1
    num = 1/n
    sum+=num
    
print(n)