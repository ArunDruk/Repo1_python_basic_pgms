import time
from functools import *
def timestamp(func):
    def inner(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,"has taken",((end-start)*1000),"millisecond")
        return res
    return inner


a=list(range(1,6001))
b=[]

@timestamp
def squares_adding(a):
    l2=[]
    for i in a:
        result=i*i
        b.append(result)
        l2=reduce(lambda x,y:x+y,b)
    #duration=((end-start)*1000)
    return l2

x=(squares_adding(a))
print(x)