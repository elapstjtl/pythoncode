'''
Author: your name
Date: 2021-03-19 12:06:47
LastEditTime: 2021-03-19 14:50:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\tool\degree_of_uncertainty.py
'''
print("输入end结束")
i = j = 0
sum = sum2 = 0
a = {}
#输入阶段
while 1:
    temp = input()
    if temp == "end":
        break
    a[i] = eval(temp)
    sum += a[i]
    i+=1
average = sum / i #计算平均值
#计算A类不确定度
for j in range(0,i):
    sum2 += (a[j]-average)*(a[j]-average)
ua = (sum2 / i /(i-1))**0.5
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

input("please input any key to exit!")


