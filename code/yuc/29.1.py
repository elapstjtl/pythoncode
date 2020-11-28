'''
Author: your name
Date: 2020-10-24 15:46:48
LastEditTime: 2020-10-24 15:52:39
LastEditors: your name
Description: In User Settings Edit
FilePath: \python\yuc\29.1.py
'''
print("请输入文件名")
filename = input()
f = open(filename,'w')
print('请输入内容【单独输入\':w\'保存退出】：')
while T:
    writesome = input()
    if writesome != 'w':
        f.write(writesome)
    else:
        break
f.close()


