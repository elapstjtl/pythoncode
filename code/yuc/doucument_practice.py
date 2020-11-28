'''
Author: your name
Date: 2020-10-24 15:15:18
LastEditTime: 2020-10-24 15:45:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\yuc\doucument_practice.py
'''

def save_file(boy,girl,count):
        file_name_boy = 'boy_'+str(count)+'.txt'
        file_name_girl = 'girl_'+str(count)+'.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()


f = open('D:/code/txt/record.txt')
boy = []
girl = []
count = 1
for eachline in f:
    if eachline[:6] != '======':
        (role,linespoken) = eachline.split(':',1)
        if role == '小甲鱼':
            boy.append(linespoken)
        if role == '小客服':
            girl.append(linespoken)   
    else:
        save_file(boy,girl,count)

        boy =[]
        girl =[]
        count+=1
save_file(boy,girl,count)