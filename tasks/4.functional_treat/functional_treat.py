print("\n",10*"*","WELCOME TO THE FUNCTIONAL TREAT",10*"*")
print()

data = []

while True:
    print("\n\n",20*"-","MENU",20*"-")
    print("1...Input")
    print("2...Display Data")
    print("3...Factorial")
    print("4...Filter Data")
    print("5...Sort Data")
    print("6...Display Dataset Statistics")
    print("7...Exit")

    print()


    choice = input("Enter your choice: ")





    if (choice == "1"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("1...Input")
        print()

        print("1...Input 1D List")
        print("2...Input 2D List")

        choice = input("\nEnter your choice: ")

        data = []

        if (choice == "1"):
            userdata = input("Enter data (separated by space): ").split()

            for value in userdata:
                data.append(int(value))

            print("Display data:", data)


        elif (choice == "2"):
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            for i in range(rows):
                userdata = input(f"Enter row {i+1}: ").split()

                row = []

                for value in userdata:
                    row.append(int(value))

                data.append(row)

            flat_data = []

            for row in data:
                for value in row:
                    flat_data.append(value)

            data = flat_data

            print("Display data:", data)


        else:
            print("Invalid input choice!")


        print(5*"=","Data entered successfully!",5*"=")










    elif (choice == "2"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("2...Display Data")
        print()

        if len(data) == 0:
            print("\n!!!Oops! No data found. Please input data first!!!")

        else:
            print("Your data:", data)

            def summary(values):
                print("\nTotal elements:", len(values))
                print("Minimum value:", min(values))
                print("Maximum value:", max(values))
                print("Sum:", sum(values))
                print("Average:", sum(values) / len(values))

            summary(data)








    elif (choice == "3"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("3...Factorial")
        print()

        def factorial(n):
            if (n < 0 or n == 0 or n == 1):
                return "Factorial not possible"

            else:
                fact = 1

                for i in range(1, n+1):
                    fact = fact * i

                return fact

        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))









    elif (choice == "4"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("4...Filter Data")
        print()

        if len(data) == 0:
            print("No data found. Please input data first!")

        else:
            user_value = int(input("Enter the value to filter: "))

            my_list = list(filter(lambda x: x >= user_value, data))

            print("Filtered data:", my_list)








    elif (choice == "5"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("5...Sort Data")
        print()

        if len(data) == 0:
            print("No data found. Please input data first!")

        else:
            print("Your data:", data)
            print()
            print("=== Sorting Options ===")
            print("\n1...Ascending Order")
            print("2...Descending Order")

            choice = input("Enter your choice: ")

            if (choice == "1"):
                print("\nOkayy--- option 1....")
                data.sort()
                print("Data sorted in ascending order:", data)

            elif (choice == "2"):
                print("\nOkayy--- option 2....")
                data.sort(reverse=True)
                print("Data sorted in descending order:", data)

            else:
                print("Invalid sorting choice!")












    elif (choice == "6"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("6...Display Dataset Statistics")
        print()

        if len(data) == 0:
            print("No data found. Please input data first!")

        else:
            def statistics(values):
                minimum = min(values)
                maximum = max(values)
                total = sum(values)
                average = total / len(values)

                return minimum, maximum, total, average

            minimum, maximum, total, average = statistics(data)

            print("Minimum:", minimum)
            print("Maximum:", maximum)
            print("Sum:", total)
            print("Average:", average)




            


    elif (choice == "7"):
        print(80*".")
        print(f"\nGotcha! You selected option {choice}....")
        print("7...Exit")
        print()
        break

    else:
        print("Invalid choice. Please try again.")


print("\n",10*"*","!!Thanks for using Functional Treat!!",10*"*")