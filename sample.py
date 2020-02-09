######################################################################################################################################################
# Takes list with duplicates and removes the duplicate entries.
#Create a dictionary, using the List items as keys.
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
######################################################################################################################################################
# l=["this","that","is","this",1,2,1]
# print(l)
# l=list(dict.fromkeys(l))
# print(l)
######################################################################################################################################################
# List reversal
# l = ["this", "that", "is", 1, 2]
# l1=l.copy()
# l1.reverse()
# print(l,l1)
######################################################################################################################################################
# # Shallow copy and deep copy
# from copy import deepcopy
# l = ["this", "that", ["is", 1, 2]]
# l1=deepcopy(l)
# l[2][0]="why"
# print(l1)
# print(l)
################################################################################################################################################
# #String reversal
# s="this is to bring to ur notice"
# s1=s[5:1:-1] #s1=s[::-1]
# print(s1,"\n",s)
################################################################################################################################################
#from imp import reload
# Below code is for pickling
import pickle
# a=[1,"his",2,"her"]
# with open("a.pickle","wb") as a_file:
#     pickle.dump(a,a_file)
#
# print(type(a_file))

# Below code is for unpickling
# with open("a.pickle","rb") as a_file:
#     d= pickle.load(a_file)
#
# print(d)
#############################################################################################################################################
# Monkey patching :  the term monkey patch refers to dynamic (or run-time) modifications of a class or module.
# In Python, we can actually change the behavior of code at run-time.
# class parent:
#     def parent1(self):
#         print("This is from parent1")
#
# def monkey_function():
#     print("This is from monkey function")
#
# #parent().parent1()
# parent.parent1=monkey_function
# print(parent.parent1())

##############################################################################################################################
l=[1,2,3,4,5]
print(l.pop(0))
print(l)