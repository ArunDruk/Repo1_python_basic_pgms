
####################################################################################################
#Lambda function Example :1 (passing a value to the function and printing it.
####################################################################################################
# g=lambda x:(3*x+1)
# print(g(3),g)

#lambda x:(3*x+1) (3)


####################################################################################################
#Lambda function Example :2 (Takes the name and printing it properly removing whitespaces and making
#only first character capital
####################################################################################################
# name=lambda fn,ln:(fn.strip().title()+" "+ln.strip().title())
# print(name("  aRUN", "kUMar " ))

####################################################################################################
#Example 3: Sorting the list using last name
####################################################################################################
L=["suhasini balu", "Priya Arun", " dhaniya chandran"]
L1=L.copy()
L.sort(key=)
# for i in L:
#     k=i.split(" ")[-1]
#     L1.append(k)

L.sort(key=lambda name:(name.split(" ")[-1]))
print(L)