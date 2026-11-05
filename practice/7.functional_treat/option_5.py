data = [[5, 2, 9], [1, 4, 7], [3, 6, 8]]
choice = input("Enter your sorting choice (1 for ascending, 2 for descending): ")

if (choice == "1"):
        print("\nOkayy--- option 1....")
        for row in data:
            row.sort()
        print("Data sorted in ascending order:", data)

elif (choice == "2"):
        print("\nOkayy--- option 2....")
        for row in data:
            row.sort(reverse=True)
        print("Data sorted in descending order:", data)

else:
        print("Invalid sorting choice!")