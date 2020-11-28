'''
Author: your name
Date: 2020-10-24 16:22:46
LastEditTime: 2020-10-24 16:28:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\yuc\29.3.py
'''

print("请输入文件名：")
file1_name = input()
print("请输入开始的行数：")
start = int(input())
print("请输入结束的行数：")
end = int(input())

f1=open('D:/code/txt/'+file1_name,'r')
for i in range(0,start-1):
    f1.readline()
for i in range(start-1,end):
    f = f1.readline()
    print(f)
f1.close()

