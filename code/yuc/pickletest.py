'''
Author: your name
Date: 2020-10-24 19:18:48
LastEditTime: 2020-10-24 19:22:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\pickletest.py
'''
import pickle
my_list = [12,214,325,325,23,5246,54]
pickle_file = open('city_key_value.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()
pickle_file = open('city_key_value.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)