# dict1 ={"name" : "Arun", "age":"Thirty one", "marital_status": "Single"}
# #print(dict.keys())
# #d1={"Job_status":"working"}
# #dict.update(d1) # Update method 1
# dict1.update(Job_status='working') #Update method 2
#
# # for i,j in dict.items():
# #     print(i,j)
# # print((dict.items()))
# #print(dict["age"])
# #print(dict.values())
#
# #list of dictionaries, storing dictionaries in a list
# L1=list() #Creating a empty list
# L1.append(dict1)
# dict2 ={"name" : "Kiran", "age":"Thirty three", "marital_status": "Single"}
# L1.append(dict2)
#
# for lists in L1:
#     for key,values in lists.items():
#         print(key +':'+values )
# ###########################################################################################################
# Passing dictionary key as an argument to the function and returing the value.
# def greeting(person):
#     return ("Hello {}".format(person))
#
#dict_name={"name":"Arun Singh","age":30}
# print(greeting(dict_name["name"]))
# ###########################################################################################################

# Deleting the key from a dictionary
# dict_name={"name":"Arun Singh","age":30}
# print (dict_name)
# del dict_name["age"]
# print(dict_name)

# ###########################################################################################################
# Converting a list to a dictionary and removing duplicates from a list using logic and list comprehension.
# Oops concept, method overriding, paramiko ssh lib, REST and Requests module, file handling a+,r+ extensions,
# CSS selectors

#Below is the code to convert list to a dictionary.
# L=[1,2,3,4,3,4]
# D={L[i]:L[i+1] for i in range(0,len(L),2)}
# print(type(D), D)

L1=[1,2,3,4,5]
L2=['a','b','c','d','e']
D1={}
for i in range(5):
    D1={L1[i]:L2[i]}
    D1.update()

print(type(D1),D1)