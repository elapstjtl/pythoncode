'''
Author: your name
Date: 2020-10-24 15:58:46
LastEditTime: 2020-10-24 16:21:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\yuc\29.2.py
'''
'''注意    f1=open('填写文件的目录文件夹+file1_name,'r')  '''
print("请输入第一个文件名：")
file1_name = input()
print("请输入第二个文件名：")
file2_name = input()

f1=open('D:/code/txt/'+file1_name,'r')
f2=open('D:/code/txt/'+file2_name,'r')
count = 0
differ = []

for line1 in f1:
    line2 = f2.readline()
    count+=1
    if line1 != line2:
        differ.append(count)

f1.close()
f2.close()

if differ == 0:
    print("完全相同")
else:
    for i in differ:
        print("第%d行不一样"%i)