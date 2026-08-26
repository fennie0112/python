a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if a >= b:
    if a >= c:
        if a >= d:
            print("The maximum number is:", a)
        else:
            print("The maximum number is:", d)
    else:
        if c >= d:
            print("The maximum number is:", c)
        else:
            print("The maximum number is:", d)
else:
    if b >= c:
        if b >= d:
            print("The maximum number is:", b)
        else:
            print("The maximum number is:", d)
    else:
        if c >= d:
            print("The maximum number is:", c)
        else:
            print("The maximum number is:", d)