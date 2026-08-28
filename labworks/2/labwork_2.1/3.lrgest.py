a = int(input("Please Enter First Number = "))
b = int(input("Please Enter Second Number = "))
c = int(input("Please Enter Third Number = "))

if(a>=b):
    if(a>=c):
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if(b>=c):
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)