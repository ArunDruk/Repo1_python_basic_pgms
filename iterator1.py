l1=['a','b','c',11,22]
myiter=iter(l1)
print(myiter)
print(next(myiter))
for i in range(4):
    print(next(myiter))