
num_1 = int(input("Enter The Value for num_1 = "))
num_2 = int(input("Enter The Value for num_2 = "))
num_3 = int(input("Enter The Value for num_3 = "))
num_4 = int(input("Enter The Value for num_4 = "))

if (num_1 == num_2 == num_3 == num_4):
    print("All numbers are equal")

elif (num_1 == num_2):
    print("num_1 is equal to num_2")

elif (num_1 == num_3):
    print("num_1 is equal to num_3")

elif (num_1 == num_4):
    print("num_1 is equal to num_4")

elif (num_2 == num_3):
    print("num_2 is equal to num_3")

elif (num_2 == num_4):
    print("num_2 is equal to num_4")

elif (num_3 == num_4):
    print("num_3 is equal to num_4")

elif (num_1 > num_2):
    if (num_1 > num_3):
        if (num_1 > num_4):
            print("num_1 is greatest")
        else:
            print("num_4 is greatest")
    else:
        if (num_3 > num_4):
            print("num_3 is greatest")
        else:
            print("num_4 is greatest")

elif (num_2 > num_1):
    if (num_2 > num_3):
        if (num_2 > num_4):
            print("num_2 is greatest")
        else:
            print("num_4 is greatest")
    else:
        if (num_3 > num_4):
            print("num_3 is greatest")
        else:
            print("num_4 is greatest")

elif (num_3 > num_1):
    if (num_3 > num_2):
        if (num_3 > num_4):
            print("num_3 is greatest")
        else:
            print("num_4 is greatest")
    else:
        if (num_2 > num_4):
            print("num_2 is greatest")
        else:
            print("num_4 is greatest")

else:
    if (num_4 > num_1):
        if (num_4 > num_2):
            if (num_4 > num_3):
                print("num_4 is greatest")
            else:
                print("num_3 is greatest")
        else:
            if (num_2 > num_3):
                print("num_2 is greatest")
            else:
                print("num_3 is greatest")
