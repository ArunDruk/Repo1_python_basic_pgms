class myclass: # Class declaration, "self" is used to access variables that belong to the class.
    def __init__(self,name,age,marital_status): #name, age, marital status are the properties of the myclass
        self.name=name
        self.age=age
        self.marital_Status=marital_status
        print(name,age,marital_status)

    def male(self): # Methods are nothing but functions inside the class
        print(f"{self.name} is accessing the method 'male' of the class 'myclass'")
        return "Hello from male method"

p=myclass("Arun",31,"Single") # Objects or instances of the class myclass
s=myclass("Soumya",24,"Single") # Objects or instances of the class myclass
print(f"{s.name} wants to marry {p.name} of age {p.age}")
s.male()

p.age=29 #Modifying properties of objects
print(f"{s.name} wants to marry {p.name} of age sorry it's {p.age}")

#Inheritance allows us to define a class that inherits all the methods and properties from another class
class mysubclass(myclass):
    def __init__(self,hobbies,favorites):
        super().__init__("aishwarya",27,"Single")
        #super(mysubclass,self).__init__("GYM","Mutton","Chicken") #Above statement and this statement both are same.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the
# methods and properties from its parent. # myclass().__init__

        self.hobbies=hobbies
        self.favorites=favorites

p1=mysubclass("Python_programming","Movies")
print("The below statement is from the mysubclass:")
print(f"{p.name} has the hobbie of doing {p1.hobbies} and also interested in {p1.favorites}")

a=issubclass(mysubclass,myclass)
b=issubclass(myclass,mysubclass)
print(a,b)

c=isinstance(p,myclass)
d=isinstance(p1,myclass)
e=isinstance(p,mysubclass)
print(c,d,e)

