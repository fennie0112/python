print("Press 1... for English")
print("Press 2... for Hindi")
print("Press 3... for Gujarati")

choice = int(input("Enter your choice = "))

match choice:

    case 1:
        print("You chose English📞", end="\n\n")
        print("Please select your option..")
        print("1. Customer Care")
        print("2. Balance Enquiry")
        print("3. Recharge")

        choice = int(input("Enter your choice = "))

        match choice:
            case 1:
                print("You selected Customer Care☎️")

            case 2:
                print("You selected Balance Enquiry💰")

            case 3:
                print("You selected Recharge💳")

            case _:
                print("Invalid choice..❗❗")


    case 2:
        print("You chose Hindi📞", end="\n\n")
        print("Please select your option..")
        print("1. Customer Care")
        print("2. Balance Enquiry")
        print("3. Recharge")

        choice = int(input("Enter your choice = "))

        match choice:
            case 1:
                print("You selected Customer Care☎️")

            case 2:
                print("You selected Balance Enquiry💰")

            case 3:
                print("You selected Recharge💳")

            case _:
                print("Invalid choice..❗❗")


    case 3:
        print("You chose Gujarati📞", end="\n\n")
        print("Please select your option..")
        print("1. Customer Care")
        print("2. Balance Enquiry")
        print("3. Recharge")

        choice = int(input("Enter your choice = "))

        match choice:
            case 1:
                print("You selected Customer Care☎️")

            case 2:
                print("You selected Balance Enquiry💰")

            case 3:
                print("You selected Recharge💳")

            case _:
                print("Invalid choice..❗❗")


    case _:
        print("Invalid choice..❗❗")