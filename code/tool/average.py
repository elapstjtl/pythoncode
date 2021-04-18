'''
Author: your name
Date: 2021-04-16 11:28:15
LastEditTime: 2021-04-16 13:26:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\tool\average.py
'''
temp = 0
a = [\
[0.06,0.08,0.10,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.08,0.06]
]
for i in a:
    sum = 0
    count = 0
    for j in range(0,len(i)):
        sum += i[j]
        count += 1
    average = sum / count
    b = average/(2.23*5)
    temp += 1
    print("%d  average = %.2f,B = %.2f"%(temp,average,b))
    

