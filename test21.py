#   Output of the program should be : {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']}
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
########## Working code #############
# def group_owners(files):
#     result={}
#     for key,value in files.items():
#         if value in result:
#             result[value].append(key)
#             break
#         else:
#             result[value]=key
#     return result
#
# print(group_owners(files))

############### Not working code ##########################
# def group_owners(files):
#     result={}
#     for a, b in files.items():
#         if b in result:
#             #result[b].append(a)
#             break
#         else:
#             result[b]=a
#     return result
#
# print(group_owners(files))

s={11,22,35,44,}
d={1:'a'}
print(type(s),type(d))
try :
    print(s[1])
except :
    print("you can't access elements in sets using index")