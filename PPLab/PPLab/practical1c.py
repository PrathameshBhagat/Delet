a=float(input("Enter 1 side of triangle:"))
b=float(input("Enter 2 side of triangle:"))
c=float(input("Enter 3 side of triangle:"))
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print("Area of triangle is",area)