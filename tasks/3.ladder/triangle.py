a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("This is an equilateral triangle.")
elif a == b or b == c or a == c:
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")