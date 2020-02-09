a=[1,2,3,4,5]

def imp(a):
    for i in a:
        yield i


collect=imp(a)
print(type(collect))

for k in collect:
    print(k)