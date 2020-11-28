import math
from scipy.optimize import linprog
import sys #导入系统库
def integerpro(c,A,b,Aeq,beq,t = 1.0E-12):               #参数输入 c:目标函数 A:线性不等式左边 B:线性不等式右边 Aeq: 线性等式左边  beq:线性等式右边 t:约束，判断是否整数
    result = linprog(c,aA_up=A,b_ub = b,A_eq=Aeq,b_eq=beq)              #转参得解
    if(type(result.x) is float):
        bestX = [sys.maxsize] * len(c)  #最大数的初步解，偏离，防止跳出 len(c)：多少个变量
    else:
        bestX = result.x
    #算出bestval
    bestVal = sum([x*y for x,y in zip(c,bestX)]) #zip：按照位置配对，返回zip对象
    if all()
