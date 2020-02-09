# fruits=['Mango'] # Define a lists name fruits
# fruits.append('apple') # Adding to the list fruits
# print (fruits)
#
# for i in range(1,5):
# 	fruits.append(i)
# print (fruits)
#
# List_Of_Fruits=fruits[:] #Copying One Lists to another
# List_Of_Fruits.append('New')
# print(List_Of_Fruits)

# print("Enter the items to be in lists : ")
# L=input()
# print (L)

# def greek(unprinted, printed):
#   while unprinted:
#     x=unprinted.pop()
#     printed.append(x.upper())
#   printed.reverse()
#   printed.sort()
#   printed.sort(reverse=True)
#   return unprinted,printed
#
#
# Unprinted=["Rock","Kane","Stone-Cold"]
# Printed=[]
#
# a,b=greek(Unprinted,Printed)
# print("This list should be empty(Unprinted): ",a)
# print("This list should contain list(printed): ",b)

####################################################################################################
#Below is the example of shallow copy
# l1=list(range(1,6))
# l2=[33,44,55,l1]
# l3=l2.copy()
# print(id(l2))
# print((id(l3)))
# print(l2, l3)
# if (id(l2)) == (id(l3)):
#     print("The address are same")

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
# l1=[1,2,3,2,1]
# l2=[11,22,33]
# print(l1)
# l1.extend(l2)
# print(l1)

# a=l1.pop()
# b=l1.count(2)
# c=l1.index(2)
# d=l1.pop(1)
# e=l1.index(2)
# print(c,d,e)

# Mentioning the index position of the value specified
l1=[1,2,3,2,1,8,2,7,2]
count_of_value=l1.count(2)
i=1
for i in range(count_of_value):
    value_pos=l1.index(2)
    value=l1.pop(value_pos)
    l1.insert(value_pos,0)
    print("The value {} is present at index position {}".format(value,value_pos))


