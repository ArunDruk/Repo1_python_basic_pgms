###########################################################################################################
# # Protecting the Account Number (Ex: Acc no - 547546543245, o/p - XXXXXXXXXX3245)
# Strings can be accessed using Indexes as well.
# def masking_account(s):
#     l=[]
#     for i in s:
#         l.append(i)
#     a=(len(l)-4)
#     m = ''.join(l[j] for j in range(-4, 0))
#     Acc="X"*a + m
#     return Acc
#
# Acc_num=input("Enter your Account number: ")
# Acc=masking_account(Acc_num)
# print("Your Account number Ending with",Acc)

#Using strings
# s="546534589467"
# k="".join(s[i] for i in range(-4,0))
# print(k)

###########################################################################################################

# import os
# import string
# print(dir(string))
# #os.mkdir("E:\letters")
# s="This is to bring to your Notice"
# #print(s.encode())
#
# #with open("E:\letters\")
# string.ascii_lowercase
####################################################################################################
########################################################################################################################
# # To find Factorial of a number
# def factorial_num(num):
#     res=num
#     for i in range(1,num):
#         res=res *(num-1)
#         num-=1
#     return res
# print(factorial_num(10))

########################################################################################################################
# # To count the Vowels (aeiou) in the String.
# s="ThisisToBringtoaeiouuuu"
# s=s.lower()
# count=0
# c=len(s)
# for i in s:
#     if (i == 'a'or i =='e' or i=='i' or i=='o'or i=='u'):
#         count+=1
# print(count,c)
########################################################################################################################
########################################################################################################################
# Reversing a list # You can use l.reverse()
#Method 1:
# l=['a',1,'b',2,'c',3,'d',4]
# lr=[]
# for i in range(1,(len(l)+1)):
#     lr.append(l[-i])
#
# print("Given list is: ",l)
# print("Reverse of a list is: ",lr)

#Method 2:
# l=['a',1,'b',2,'c',3,'d',4]
# lr=l.copy()
# lr.reverse()
# print(lr)
########################################################################################################################
# Program to check if Tupple contains any None value
# t=(10, 4, None,5, 6)
# for i in t:
#     if i is None:
#         print("Contains None value")
#         break

# a=(3,)
# b=not any(a)
# print(b)
###########################################################################################################
# class myclass: # Class declaration, "self" is used to access variables that belong to the class.
#     def __init__(self,name,age,marital_status): #name, age, marital status are the properties of the myclass
#         self.name=name
#         self.age=age
#         self.marital_Status=marital_status
#
#     def male(self): # Methods are nothing but functions inside the class
#         print(f"{self.name} is accessing the method 'male' of the class 'myclass'")
#
#
#
# p=myclass("Arun",31,"Single") # Objects or instances of the class myclass
# s=myclass("Soumya",24,"Single") # Objects or instances of the class myclass
# print(f"{s.name} wants to marry {p.name} of age {p.age}")
# s.male()
#
# p.age=29 #Modifying properties of objects
# print(f"{s.name} wants to marry {p.name} of age sorry it's {p.age}")
#
# #Inheritance allows us to define a class that inherits all the methods and properties from another class
# class mysubclass(myclass):
#     def __init__(self,hobbies,favorites):
#         super().__init__(hobbies,favorites)
# # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the
# # methods and properties from its parent. # myclass().__init__
#
#         self.hobbies=hobbies
#         self.favorites=favorites
#
# p1=mysubclass("Python_programming","Movies")
# print("The below statement is from the mysubclass:")
# print(f"{p.name} has the hobbie of doing {p1.hobbies} and also interested in {p1.favorites}")
#
# a=issubclass(mysubclass,myclass)
# b=issubclass(myclass,mysubclass)
# print(a,b)
#
# c=isinstance(p,myclass)
# d=isinstance(p1,myclass)
# e=isinstance(p,mysubclass)
# print(c,d,e)
###########################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.keys import keys
#
# driver=webdriver.Chrome
# driver.get("http://support.microsoft.com")




