# # lambda argument_list : expression
# n=int(input("Enter a num: "))
# s=lambda n:n*n
# print(f'Square of {n} is:', s(n))

#filter(function,sequence)
#We can use filter() function to filter values from the given sequence based on some condition.
#Filter function will only return the value for the function which is TRUE
# a=[]
# for i in range(0,10):
#     a.append(i)

# l1=list(filter(lambda x: x%2==0,a))
# l2=list(filter(lambda x: x%2!=0,a))
# print("List of Even numbers between 0-10",l1)
# print("List of odd numbers between 0-10",l2)

# map(function,sequence)
#For every element present in the given sequence,apply some functionality and generate
#new element with the required modification. For this requirement we should go for map function


#a=[]
# for i in range(0,10):
#     a.append(i)
# l1=list(map(lambda x: x*x,a))
# print("List of Squares for the numbers between 0-10",l1)

# Ex:2, Map function use to apply some expression only to the second element in all the list elements
l=[("Arun",29),("Sharmila",25)]
c_to_f=lambda x:(x[0],((9/5)*x[1])+32)
l2=list(map(c_to_f,l))
print(l2)

#reduce(function,sequence)
#reduce() function reduces sequence of elements into a single element by applying the specified function.
#reduce() function present in functools module and hence we should write import statement.

# from functools import *
# l1=list(range(0,10))
# l2=reduce(lambda x,y:x+y,l1)
# print(l2)

# In the below example decor is a decorator function which takes function as an argument
# def decor(func):
#     def inner(name):
#         if name=="Sunny":
#             print("Hello Sunny Bad Morning")
#         else:
#             func(name)
#     return inner
#
# @decor
# def wish(name):
#     print("Hello",name,"Good Morning")
#
# wish("Durga")
# wish("Ravi")
# wish("Sunny")
