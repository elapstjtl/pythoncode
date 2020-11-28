'''
Author: your name
Date: 2020-10-25 15:56:12
LastEditTime: 2020-10-25 16:11:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\luogu\averange_classic.py
'''
n,k= map(int,input().split(' '))
ok = 0
count1 = 0
notok =0
count2 = 0
for i in range(1,n+1):
    if i % k == 0:
        ok +=i
        count1+=1
    else:
        notok+=i
        count2+=1
ok = ok/count1
notok = notok/count2
print('%.1f %.1f'%(ok,notok))



