num = int(input("Enter a valur for num = "))

if (num % 2 == 0):
    print(f"{num} is an even integer")

elif(num % 2 != 0):
    print(f"{num} is an odd integer")

elif (num == 0):
    print("You entered Zero")

else:
    print("please enter valid choice")