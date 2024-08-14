import math
class Sphere:

    PI = math.pi

    def _init_(self , radius):
            self.radius = radius

    def diameter( self ):
        return 2*self.radius

    def surafceArea( self ):
        return 4*self.PI*(self.radius**2)

    def volume( self ):
        return (4/3)*self.PI(self.radius**2)

obj = Sphere(5)
print("Diameter of Circle = " , obj.diameter())
print("Surafcearea of Circle = " , obj.surafceArea())
print("volume of Circle = " , obj.volume())

'''

'''

class Account:

    balance = 0

    def _init_(self):
        self.name = input("Enter your Name = ")
        self.age = int(input("Enter your Age = "))
        self.accountNo = input("Enter your Account No = ")

    def deposit( self ):
        amount = int(input("Enter Amount you want to deposit = "))
        self.balance += amount
        print("Amount Deposited")
        self.viewBalance()

    def withdraw( self ):

        amount = int(input("Enter Amount you want to withdraw = "))

        if( amount > self.balance ):
            print(" cannot Withdraw ")
            self.viewBalance()
        else:
            self.balance -= amount
            print("not Suffient Balance")
            self.viewBalance()


    def viewBalance( self ):
        print("\n ------------------------------------------ \n")
        print("Name = " , self.name)
        print("Age = " , self.age)
        print("Account Number = " , self.accountNo)
        print("Current balance = " , self.balance)
        print("\n ------------------------------------------ \n")

amit = Account()
amit.deposit()
amit.withdraw()

'''

'''
class Person:

    def _init_(self , name , city ):
        self.name = name
        self.city = city

    def display(self):
        print(f"Name = {self.name}")
        print(f"City = {self.city}")

class Student(Person):
    def _init_(self , name  , city , roll , dept ):
        super()._init_(name , city)
        self.roll = roll
        self.dept = dept

    def display(self):
        super().display()
        print(f"Roll = {self.roll}")
        print(f"Deptartment = {self.dept}")

class Teacher(Person):
    def _init_(self , name  , city ,  desig , dept ):
        super()._init_(name , city)
        self.desig = desig
        self.dept = dept

    def display(self):
        super().display()
        print(f"Designation = {self.desig}")
        print(f"Dept = {self.dept}")

amit = Student("amit Anandpara" , "Wardha"  , 203 , "computer")
amit.display()

print("\n-------------------\n")

teacher = Teacher("Sandesh JAin" , "Wardha"  , "Assisstant Professor" , "computer")
teacher.display()

'''

class Fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()

class Mango(Fruit):
    def taste(self):
        return "Sweet"
    def rich_in(self):
        return "Vitamin A"
    def color(self):
        return "Yellow"

class Cherry(Fruit):
    def taste(self):
        return "Sour or Sweet"
    def rich_in(self):
        return "Vitamin C"
    def color(self):
        return "Cherry"

mang = Mango()
print( mang.taste() , mang.rich_in(), mang.color() )
org = Orange()
print( org.taste() , org.rich_in(), org.color() )

'''
