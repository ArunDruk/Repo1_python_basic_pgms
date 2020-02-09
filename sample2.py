# Print the ascending order of the given list.

# a=[4,2,8,7,22,17]
# copy_list=a.copy()
# new_list=[]
# while a:
#     b=min(a)
#     c=a.index(b)
#     asc=a.pop(c)
#     new_list.append(asc)
#
# print("The given list is: {0}".format(copy_list))
# print("The ascending order of the given list is: {0}".format(new_list))

# n=int(input("Enter a num: "))
# def factorial_num(n):
#     if(n==0):
#         return 1
#
#     else:
#         result=n*factorial_num(n-1)
#         return result
#
# #print("Factorial of", n ,"is" ,factorial_num(n))
# #print("Factorial of {0} is".format(n) ,factorial_num(n))
# print(f'Factorial of {n} is',factorial_num(n))
####################################################################################################
#Below is the example of shallow copy
# l1=list(range(1,6))
# l2=[33,44,55,l1]
# l3=l2.copy()
#
# print(l1,"\n",l2,"\n",l3,"\n")
# l2[3][4]=9
# print(l1,"\n",l2,"\n",l3,"\n")
####################################################################################################
#Below is the example of deep copy, even though the elements are changed in the sublist of a list, the copied list will not be changed.
# from copy import deepcopy
# l1=list(range(1,6))
# l2=[33,44,55,l1]
# l3=deepcopy(l2)
#
# print(l1,"\n",l2,"\n",l3,"\n")
# l2[3][4]=9
# print(l1,"\n",l2,"\n",l3,"\n")

####################################################################################################
# To find the start and end time of a function
import time
from functools import *
a=list(range(1,6001))
b=[]
def squares_adding(a):
    #start=time.asctime(time.localtime(time.time()))
    start=time.time()
    l2=[]
    print(start)

    for i in a:
        result=i*i
        b.append(result)
        l2=reduce(lambda x,y:x+y,b)
    #end=time.asctime(time.localtime(time.time()))
    end=time.time()
    #print(squares_adding.__name__)
    print(end)
    duration=((end-start)*1000)
    return l2,duration

x,y=(squares_adding(a))
print("The timetaken for this function to execute is",y,"sec")

####################################################################################################














