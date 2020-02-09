#!/usr/bin/python
def add(num1,num2):
	print ("Sum is : ",num1+num2)
	return num1+num2

op= int (input ("Enter the operation as shown below:  1-> add,2->sub,3->Mul :  "))
num1 = int(input("enter the first number"))
num2 = int(input("enter the sec number"))
if op ==1:
	print(add(num1,num2))
elif op==2:
	sub(num1,num2)
elif op==3:
	mul(num1,num2)
else:
	print("Enter number either 1, 2 or 3")





