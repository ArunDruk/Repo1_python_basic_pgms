
def decor_fun(func):
    def inner(*args):
        with open("writing_results.txt",'w') as fw:
            fw.write(case1())
    return

@decor_fun
def case1():
    return "This is from case1"

def case2():
    return "This is from case2"

