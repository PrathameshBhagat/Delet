#With Argument and Return Type
'''
def add(a,b):
    sum = a+b
    return sum

a = int(input("Enter a Number = "))
b = int(input("Enter a another Number = "))

result = add(a,b)
print(result)
'''

#Without Argument and with Return Type

'''
def add():
    num1 = int(input("Enter a Number = "))
    num2 = int(input("Enter a another Number = "))
    return num1+num2

print("Without Arguments \n")
print(add())
'''

#With Argument and Without Return Type

'''
def add(a,b):
    result = a+b
    print(result)

print("Without Return value ")

num1 = int(input("Enter a Number = "))
num2 = int(input("Enter a another Number = "))
add(num1 , num2)
'''

#Without Argument and Without Return Type


def add():
    num1 = int(input("Enter a Number = "))
    num2 = int(input("Enter a another Number = "))
    print( num1 + num2 )


print("Without Return value and Arguments")
add()
