x = int(input("Enter a valur for x = "))
y = int(input("Enter a valur for y = "))

if (x>y):
    print(f"{x} is greater than {y}")

elif(x<y):
    print(f"{y} is greater than {x}")

elif (x==y):
    print(f"{x} and  {y} are equal ")

else:
    print("please enter valid value")