# import numpy as np
# a=["Infy","Facebok","Wipro"]
# x=np.arange(len(a))
# print(x+2)

# def first_last6(a):
#     if a[0]==6 or a[-1]==6:
#         return True
#     else:
#         return False
#
# print(first_last6([6,1,2,4]))

# a=[6,1,2,4]
# print(a[len(a-1)])


# To read each character in a string.
# def double_char(a):
#     r = " "
#     for c in a:
#         print(c)
#         r+= c*2
#     return r
#
# print(double_char('AAbb'))

#To count the number of even digits in a list
# def count_evens(a):
#     i=len(a)
#     c=0
#     for i in range(0,i):
#         if(a[i]%2==0):
#            c+=1
#     return c
#
# print(count_evens([1,1,7,3,9]))

#To count the number of odd digits in a list, the logic for for loop is changed.
# def count_odd(a):
#     #i=len(a)
#     c=0
#     for i in a:
#         if(i%2==1):
#            c+=1
#     return c
#
# print(count_odd([1,2,4,3,9]))

#Return True if the string "cat" and "dog" appear the same number of times in the given string or else False.
# def cat_dog(a):
#     count_cat=0
#     count_dog=0
#     count_cat=a.count("cat")
#     count_dog=a.count("dog")
#     if count_cat == count_dog:
#         return True
#     else:
#         return False
#
# print(cat_dog('1cat1cadodog'))

# for a in str.split():
#     print(a)

#String count
str="ArunKiranarununarun"
str=str.lower()
r=str.replace("arun","kiran")
k=str.replace("arun","kiran",1) #number of times it has to replace, by default it will replace completely.
#print(str,r,k)
# a=str.count("arun")
#a=str.count("arun",0,4) #"arun" is to search inside the str and '0' is the start position and '4' is the end position to search for in the string.
#print(a)
f=str.find("kiran") #find : If substring exists inside the string, it returns the index of first occurence of the substring else returns -1.
print(f)




