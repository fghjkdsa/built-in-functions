# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:08:41 2020

@author: Administrator
"""

def add(x,y,fun):
    return fun(x)+fun(y)
print(add(-6,3,abs))

############   map的使用   ###############
def f(x):
    return x*x

l = [1,2,3,4,5,6,7,8]

r = map(f,l)
#from collections import Iterator
#print(isinstance(r,Iterator))
print(list(r))

s = list(map(str,l))
# 等价于
s0 = [str(x) for x in l]


# 传入多个列表
a = [1,2,3]
b = [11,12,13]
def f(x,y):
    return x*y
r1 = list(map(f,a,b)) # 对应元素相乘
#等价于
r2 = [x*y for x,y in zip(a,b)]
# 不等价于
r3 = [x*y for x in a for y in b]

############   reduce的使用   ###############
# reduce的使用
from functools import reduce
a = [1,2,3,4,5,6]
def f(x,y):
    return x+y
s = reduce(f,a)
print(reduce.__doc__)
print(s)


def f2(x,y):
    return x*10+y
r0 = reduce(f2,a)

# 等价于
b = list(map(str,a))
r = int(''.join(b))


############   filter的使用   ###############
# 过滤函数的使用，保留返回结果为True的元素，不一定非是1，还可以是非空字符串等
def is_odd(x):
    return x%2==1

a = [1,2,3,4,5,6]
a = range(30)
r = list(filter(is_odd,a)) # 保留奇数

# 保留非空字符串
def f(x):
#    return x.strip() and x # 不能这么写,'NoneType' object has no attribute 'strip'
    return x and x.strip()



a = ['a','','b',None,'  ']
r = list(filter(f,a))



############   sorted的使用   ###############

a = [1,3,2,6,8,5]
a1 = sorted(a) # 正序
a2 = sorted(a,reverse=True) # 倒序 逆序

# sorted 自定义排序
# 按绝对值大小排序
a = [1,3,-2,6,8,-5]
a3 = sorted(a,key=abs) # key为函数引用 如key=str.lower # 字符串转为小写


####################### 匿名函数 #######
f = lambda a,b,c:a+b+c
print(f(1,2,3))

a = list(map(f,[1,2],[3,4],[5,6]))
a = list(map(lambda a,b,c:a+b+c,[1,2],[3,4],[5,6]))

# 对对象排序
class Student:
    def __init__(self,n,a):
        self.age = a
        self.name = n

stu1 = Student('a',1000)
stu2 = Student('b',2)
stu3 = Student('c',3)
r = sorted([stu1,stu2,stu3],reverse=True,key=lambda x:x.age)# 按照年龄排序
for x in r:
    print(x.name,x.age)










