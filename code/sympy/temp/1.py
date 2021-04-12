'''
Author: your name
Date: 2021-04-11 18:35:11
LastEditTime: 2021-04-12 19:38:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythoncode\code\sympy\temp\1.py
'''
from sympy import *
from sympy import init_printing

init_printing(use_unicode=True)

r,h,y,z = symbols('r h y z')
b = sqrt(((r**2-h**2)*(y)**2*((z - h)**2 - r**2)+(y)**2*(h*z - h**2+r**2)**2)/((z-h)**2+r**2),2)
a = (r*r - h*h +(h*(z) - h*h + r*r)**2 / (((z) - h)**2+r*r))**0.5

expr = pi*a*b/4
cancel(expr)
pprint(expr)