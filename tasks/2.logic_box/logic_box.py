print("============================================================")
print(" \tWelcome to the Pattern & Number Logic Box!")
print("============================================================")

while True:
    print("\nPlease select an option:")
    print("1. Generate a Pattern ")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    choice = input("Enter your choice : ")

    match choice:
        case "1":
            print("\n----------------------------- PATTERN TIME!---------------------------------")
    
            print("\nPlease select a pattern type:")
            print("\n1. Square Pattern")
            print("2. Star Triangle")
            print("3. Number Repeat Triangle")
            print("4. Number Increment Triangle")
            print("5. Continuous Number Triangle")
            print("6. Binary Column Triangle")
            print("7. Binary Row Triangle")
            print("8. zebra Triangle")
            print("9. Zero r-c Triangle")
            print("10. Reverse Number Triangle")
            print("11. Inverted Triangle")
            print("12. Pyramid Pattern")

            choice = int(input("\nEnter your choice : "))
            r = int(input("Enter the number of rows for the pattern: "))

    
            match choice:
                case 1:
                    print("\nSquare Pattern:")
                    for i in range(1, r+1):
                        for j in range(1, r+1):
                            print("*", end=" ")
                        print()
                    print("_________________________________")

                case 2:
                    print("\nStar Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print("*", end=" ")
                        print()
                    print("_________________________________")
                case 3:
                    print("\nNumber Repeat Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print(i, end=" ")
                        print()
                    print("_________________________________")
                case 4:
                    print("\nNumber Increment Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print(j, end=" ")
                        print()
                    print("_________________________________")

                case 5:
                    print("\nContinuous Number Triangle:")
                    k = 0
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print(k, end=" ")
                            k += 1
                        print()
                    print("_________________________________")

                case 6:
                    print("\nBinary Column Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            if j % 2 == 0:
                                print(0, end=" ")
                            else:
                                print(1, end=" ")
                        print()
                    print("_________________________________")

                case 7:
                    print("\nBinary Row Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            if i % 2 == 0:
                                print(0, end=" ")
                            else:
                                print(1, end=" ")
                        print()
                    print("_________________________________")

                case 8:
                    print("\nZebra Triangle:")
                    k = 1
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            if i % 2 != 0:
                                print(k, end=" ")
                                k += 1
                            else:
                                print("*", end=" ")
                        print()
                    print("_________________________________")

                case 9:
                    print("\nZero r-c Triangle:")
                    for i in range(0, r):
                        for j in range(0, i+1):
                            if i == j:
                                print("0", end=" ")
                            else:
                                print(i, end=" ")
                        print()
                    print("_________________________________")

                case 10:
                    print("\nReverse Number Triangle:")
                    for i in range(0, r):
                        k = 0
                        for j in range(0, i+1):
                            print(r-1-k, end=" ")
                            k += 1
                        print()
                    print("_________________________________")

                case 11:
                    print("\nInverted Triangle:")
                    for i in range(r, 0, -1):
                        for j in range(i, 0, -1):
                            print(j, end=" ")
                        print()
                    print("_________________________________")

                case 12:
                    print("\nPyramid Pattern:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print(i, end=" ")
                        print()
                    for i in range(r-1, 0, -1):
                        for j in range(i, 0, -1):
                            print(i, end=" ")
                        print()
                    print("_________________________________")

                case _:
                    print("Invalid pattern choice.")

            
        case "2":
            print("\n---------------------------NUMBER ANALYSIS ZONE-----------------------------")

            start = int(input("\nEnter the starting number of the range: "))
            end = int(input("Enter the ending number of the range: "))
            print()

            sum = 0

            for num in range(start, end + 1):
                print(f"Number {num} is: ", "even" if num % 2 == 0 else "odd")
                sum += num
            
            print(f"\nSum of all numbers from {start} to {end}: {sum}")
            print("__________________________________________________________________________________")
            
        case "3":
            break
        case _:
            print("----------Oops! That choice went on vacation!  Try again!-------------------")


print("============================================================")
print("  Thank you for using the Pattern & Number Logic Box!")
print("============================================================")
print("============================================================")
print("                     SEE YOU AGAIN! ")
print("============================================================")
