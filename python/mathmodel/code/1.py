'''
Author: your name
Date: 2020-11-07 19:44:02
LastEditTime: 2020-11-07 19:45:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\math\1.py
'''
import math
#`根据不等式定理当s = 15r+（-math.pi/2-2）r**2`
r = -15/(-math.pi-4)
print(f"r={r}")
s = 15*r-2*r*r-math.pi*r*r/2
print(f"s={s}")
l = (15-math.pi*r-2*r)/2
print(f"l={l}")