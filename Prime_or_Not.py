# To take the range and print the prime numbers


x=int(input("Enter a start number from which you need the prime numbers: "))
y=int(input("Enter a End number till which you need the prime numbers: "))
for x in range(x,y):
    if ((x%2 ==0) or (x%3==0) or (x%5==0)) ==0:
        print(x,end=",")
