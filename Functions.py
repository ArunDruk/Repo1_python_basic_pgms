#***********************************
# #Function retruning a single value
# def my_function(fname):
#   fullname= fname + " "+ "Refsnes"
#   return fullname
#
# print(my_function("Emil"))
#***********************************

#***********************************
# #Function retruning a Dictionary
# def my_function(fname,lname):
#   fullname={"first":fname,"last":lname}
#   return fullname
#
# print(my_function("Emil","Refsnes"))
#***********************************

#***********************************
#Passing a list as an argument to a function and returning back a list with names in capitals

# def greek(wwe_stars):
#   print(type(wwe_stars))
#   stars=[]
#   for i in wwe_stars:
#     stars.append(i.upper())
#   return stars
#
# names=["Rock","Kane","Stone-Cold"]
# y=greek(names)
# print(y)
#***********************************
#pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value.
# names=["Rock","Kane","Stone-Cold"]
# print(names.pop())
# print(names)
#***********************************

#***********************************
#Taking a list as a argument and poping the elements and saving it in other list and returning both lists
# def greek(unprinted,printed):
#   while unprinted:
#     i=0
#     x=unprinted.pop(i) #By default pop returns the last element of the list, if we want to pop elements in the same manner, use a variable i=0 then increment by i+=1
#     i+=1
#     printed.append(x.upper())
#   return unprinted,printed
#
#
# Unprinted=["Rock","Kane","Stone-Cold"]
# Printed=[]
#
# a,b=greek(Unprinted,Printed)
# print("This list should be empty(Unprinted): ",a)
# print("This list should contain list(printed): ",b)
#***********************************

def greek(unprinted, printed):
  while unprinted:
    x=unprinted.pop()
    printed.append(x.upper())
  printed.reverse()
  printed.sort()
  printed.sort(reverse=True)
  return unprinted,printed


Unprinted=["Rock","Kane","Stone-Cold"]
Printed=[]

a,b=greek(Unprinted,Printed)
print("This list should be empty(Unprinted): ",a)
print("This list should contain list(printed): ",b)