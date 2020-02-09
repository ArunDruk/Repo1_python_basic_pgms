# def fib(num):
#     for i in range(0,num):
#         yield i
#         i=i+1
#
# y=fib(10)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
#
# # l1=["Get's it Go",1,2,3,4,5]
# #
# #
# # def list_reversing(l1):
# #     return [(i for i in reversed(l1))]
# #
# #
# l2=list()
# l2=list_reversing(l1)

import re
# from copy import deepcopy
# l1=[1,2,[33,44]]
# l2=deepcopy(l1)
# l1[2][1]=99
# print(l1,l2)

#a,b=0,1
def fibo_series(a,b):
    for i in range(0,11):
        break
    yield a
    a,b=b,a+b

print(fibo_series(0,1))







