age = int(input("Please Enter Your age = "))

if(age<=12):
    if(age>=0):
        print("You are in Children Category.....")
    else:
        print("Error.....!")

elif(age<=19):
    if(age>=13):
        print("You are in Teenage Category...")
    else:
        print("Error...!!")

elif(age<=59):
    if(age>=20):
        print("You are in Adult Category...")
    else:
        print("Error...!!")

else:
    print("You are in Senior Category...")