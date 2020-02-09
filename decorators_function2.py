def printout(func):
    def inner(args):
        if args=="Swapna":
            print("Hi",args,"Bad Morning")
            return
        func(args)
    return inner

@printout
def printing(a):
    print("Hi",a,"Good Morning")

printing("Arun")
printing("Swapna")