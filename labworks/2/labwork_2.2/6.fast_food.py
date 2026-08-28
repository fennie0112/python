print("Press 1... to order a Sandwich🥪")
print("Press 2... to order a Pizza🍕")
print("Press 3... to order a Burger🍔")

choice = int(input("Enter your choice = "))

match choice:

    case 1:
        print("You ordered a Sandwich🥪", end="\n\n")
        print("Please select your Sandwich type..", end="\n")
        print("1. Veg Sandwich")
        print("2. Cheese Sandwich")
        print("3. Grilled Sandwich")

        sandwich_choice = int(input("Enter your choice = "))

        match sandwich_choice:
            case 1:
                print("You ordered Veg Sandwich🥪")

            case 2:
                print("You ordered Cheese Sandwich🧀🥪")

            case 3:
                print("You ordered Grilled Sandwich🥪")

            case _:
                print("Invalid Sandwich choice..❗❗")


    case 2:
        print("You ordered a Pizza🍕")
        print("Please select your Pizza type..", end="\n")
        print("1. Loaded Pizza")
        print("2. Farmhouse Pizza")
        print("3. Peppy Paneer Pizza")

        pizza_choice = int(input("Enter your choice = "))

        match pizza_choice:

            case 1:
                print("You ordered Loaded Pizza🍕")

            case 2:
                print("You ordered Farmhouse Pizza🍕")

            case 3:
                print("You ordered Peppy Paneer Pizza🍕")

            case _:
                print("Invalid Pizza choice..❗❗")


    case 3:
        print("You ordered a Burger🍔")
        print("Please select your Burger type..", end="\n")
        print("1. Veg Burger")
        print("2. Cheese Burger")
        print("3. Paneer Burger")

        burger_choice = int(input("Enter your choice = "))

        match burger_choice:

            case 1:
                print("You ordered Veg Burger🍔")

            case 2:
                print("You ordered Cheese Burger🧀🍔")

            case 3:
                print("You ordered Paneer Burger🍔")

            case _:
                print("Invalid Burger choice..❗❗")


    case _:
        print("Invalid choice..❗❗")