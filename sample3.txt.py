# Function decorator

# def check(func):
#     def inner(a,b):
#         if b==0:
#             print("Division by zero is not possible")
#         else:
#             func(a,b)
#     return inner
#
# @check
# def div_num(a,b):
#     return a/b
#
# print(div_num(4,3))


# def nums(*n):
#     pass
#
# nums(1,2,3,4,5)

# def nums_list(**l2):
#     print(*l2)
#     print(l2)
#
# nums_list(a="Apple",b="Ball",c="Cow")

#Decorator function to calculate the time taken by the function to execute
# import time
# from functools import *
# def timestamp(func):
#     def inner(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         end=time.time()
#         print(func.__name__,"has taken",((end-start)*1000),"millisecond")
#         return res
#     return inner
#
#
# a=list(range(1,6001))
# b=[]
#
# @timestamp
# def squares_adding(a):
#     l2=[]
#     for i in a:
#         result=i*i
#         b.append(result)
#         l2=reduce(lambda x,y:x+y,b)
#     #duration=((end-start)*1000)
#     return l2
#
# x=(squares_adding(a))
# print(x)
import random
def gen_func(num):
    x=random.randrange(1,11)

y=gen_func(10)
print(y)

from imp import reload
reload()