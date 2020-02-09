# Method Overloading means two or more methods having same name but different meaning
# Python doesn't support method overloading but it takes the latest method defined

# class base_class:
#     def sum(a,b):
#         return a+b
#
# class sub_class(base_class):
#     pass
#
# b1=sub_class
# x=b1.sum(8,4)
# print(x)

# class add:
#     def __init__(self,a,b):
#         self.__a=a
#         self.__b=b
#
# me=add(3,4)

D={1:'a',2:'b',3:'c'}
# Printing only keys from D
# for i in D:
#     print(i)

#Printing key and its value from D
# for k,v in D.items():
#     print("Key is {} and the corresponding value is {}".format(k,v))

#Printing only values from D
# for v in D.values():
#     print(v)




####################################################################################################
# Difference between find() and index() method
# a="Name is Arun"
# b=a.find("Kiran")
# try:
#     a.index("Kiran")
# except ValueError:
#     print("substring not found")
#
# print(b)

####################################################################################################
# Difference between find() and rfind() methods
# a="this that and again this"
# k=a.find("this") # Return the index number where it was found first
# l=a.rfind("this") # Returns the index number where it was found last.
# print(k)
# print(l)

####################################################################################################