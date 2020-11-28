'''
Author: your name
Date: 2020-10-24 16:29:48
LastEditTime: 2020-10-24 16:40:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\29.5.py
'''
'''注意    f1=open('填写文件的目录文件夹+file1_name,'r')  '''
print("请输入文件名：")
file1_name = input()
print("被替换的词：")
old = input()
print("代替的词：")
new = input()

content = []

f=open('D:/code/txt/'+file1_name,'r',encoding='UTF-8')
for eachline in f:
    if old in eachline:
        eachline = eachline.replace(old,new)
    content.append(eachline)
f.close()
f2 = open('D:/code/txt/'+file1_name,'w',encoding='UTF-8')
f2.writelines(content)
f2.close()

