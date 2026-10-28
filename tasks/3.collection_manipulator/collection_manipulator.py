print("\n########### Welcome to the Student Collection Manipulator! ###########\n")


students = [
    {
        "rollno": "101",
        "name": "Peter Parker",
        "age": 25,
        "grade": "A+",
        "dob": "2001-10-10",
        "sub": {"C", "Python", "C++", "PHP"}
    },

    {
        "rollno": "102",
        "name": "Miles Morales",
        "age": 27,
        "grade": "A++",
        "dob": "1999-10-03",
        "sub": {"C", "Python", "Java"}
    }
]



while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    
    if choice == 1:
        print("\n--- Add Student ---")

        rollno = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))                    
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = set(input("Subjects (comma-separated): ").split(","))

        
        student = {
            "rollno": rollno,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "sub": subjects
        }

    
        tuple_info = (rollno, dob)

        students.append(student)                     
        print("\nStudent added successfully!")
        print("\n",80*"<")



    
    elif choice == 2:
        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No students found.")
        else:
            for s in students:
              print() 
              print() 
              print(f"Student ID : {s['rollno']}")
              print(f"Name       : {s['name']}")
              print(f"Age        : {s['age']}")
              print(f"Grade      : {s['grade']}")
              print(f"Date of Birth: {s['dob']}")
              print(f"Subjects   : {', '.join(s['sub'])}")
        print(f"\n",80*"<")


    
    elif choice == 3:
        print("\n--- Update Student Information ---")
        roll = input("Enter Student ID: ")

        found = 0
        for s in students:
            if (s["rollno"] == roll):
                found = 1
                print("\n******Student Found!*******")

                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Grade")
                print("4. Update Subjects")
               

                choice = int(input("Enter choice: "))

                if (choice == 1):
                    s["name"] = input("New Name: ")
                elif (choice == 2):
                    s["age"] = int(input("New Age: "))
                elif (choice == 3):
                    s["grade"] = input("New Grade: ")
                elif (choice == 4):
                    s["sub"] = set(input("New Subjects (comma-separated): ").split(","))
                else:
                    print("Invalid option!")

                print("******Student updated successfully!******")
            
                print(f"\n",80*"<")
                break

            else:
                print("!!!!!!!!!!!Student Not Found!!!!!!!!!!!!")
                print(f"\n",80*"<")

       

    
   
    elif choice == 4:
        print("\n--- Delete Student ---")
        roll = input("Enter Student ID: ")

        for i in range(len(students)):
            if (students[i]["rollno"] == roll):
                del students[i]

                print("Student deleted successfully!")
                print(f"\n{'<' * 80}")
                break
        else:
            print("Student not found!")


  
    elif choice == 5:
        print("\n--- Subjects Offered ---")
    
        all_sub = set()
    
        for s in students:
            all_sub.update(s["sub"])
    
        print("Unique Subjects:")
        print()
        for sub in all_sub:
            print( sub)


    
    elif choice == 6:
        print("\n",80*"<")
        print("\n###### That's a wrap! See you next time! ######")
        print("\n",80*">")
        break

    else:
        print("\nInvalid choice! Please try again.")
        print("\n",80*">")