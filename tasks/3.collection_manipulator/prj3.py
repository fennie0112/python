 
print("\n\nWelcome to the Student Collection Manipulator!")

students = [
    
    {
      "rollno" : "1",
      "name"  :  "jalak",
      "age"    : "18",
      "grade"  : "AA",
      "dob"    : "2007-09-22",
      "sub"    : "maths,science,eng"
    },


    {
          "rollno" : "2",
          "name"  :  "alice",
          "age"    : "17",
          "grade"  : "BB",
          "dob"    : "1999-10-03",
          "sub"    : "c,python,java"
        }
]



while True:

    print("\n\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:

         print("\n\n1. Add Student")
         print()
         print("Add Details of student:-")
         print()

         student = {
             "rollno": input("Student ID: "),
             "name": input("Name: "),
             "age": int(input("Age: ")),
             "grade": input("Grade: "),
             "dob": (input("Date of Birth (YYYY-MM-DD): ")),
             "sub": set(input("Sub(comma-separated): ").split(",")),
         }

         students.append(student)

         print("Student added successfully!")
         



    elif (choice==2):

          print("\n\n2.Display All students")
          print()


          for student in students:
                print("Student ID:", student["rollno"])
                print("Date of Birth:", student["dob"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("Subjects:", student["sub"])
            

    elif(choice==3):
            print("\n\n3.Update students Information")
            print()

            roll = (input(" enter student  ID = "))

            for student in students:
               if (roll == student["rollno"]):

                 print("Student Found!!")

                 print("\n\n1. Update id")
                 print("2. Update name")
                 print("3. Update age")
                 print("4. Update grade")
                 print("5. Update dob")
                 print("6. Update subjects")

                 update = int(input("Enter your choice: "))

                 if update == 1:
                     student["rollno"] = int(input("Enter new ID: "))
 
                 elif update == 2:
                     student["name"] = input("Enter new name: ")
 
                 elif update == 3:
                     student["age"] = int(input("Enter new age: "))
 
                 elif update == 4:
                     student["grade"] = input("Enter new grade: ")
 
                 elif update == 5:
                     student["dob"] = input("Enter new dob: ")
 
                 elif update == 6:
                     student["sub"] = set(input("Enter new subjects: ").split(","))
 
                 else:
                     print("You Entered Invalid choice ...")
                     print("Try Again....")
 
                 print("Student updated successfully!")
                 


    elif choice == 4:
     print("\n\n4.Delete Student........")
     print()

     roll = input("Enter Student ID: ")

     for student in students:
        if student["rollno"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            break
     else:
        print("No student found with that ID.")
    


    elif choice == 5:
     print("\n\n5.Display Subjects Offered........")
     print()

     subjects = set()
     for student in students:
        subjects.update(student["sub"].split(","))

        for subject in subjects:
         print(subject)
     

    elif (choice==6):
         print("\n\n See you next time!") 
         break



    else:
         print("\n\nYou Entered Invalid choice")
         break
