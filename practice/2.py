print("Welcome to the Interactive Personal Data Collector!",end="\n\n")

yourname = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav = int(input("Please enter your favorite number: "))

print("\n\nThank you! Here is the information we collected:")

print("Name:", yourname,"(type:", type(yourname), ")")
print("Age:", age,"(type:", type(age), ")")
print("Height:", height,"(type:", type(height), ")")
print("Favorite Number:", fav,"(type:", type(fav),")",end="\n\n")
print("You Birthyear is approximatery :", 2026 - age,"(based on your age:", age, ")", end="\n\n")
print("Thank you for using the Resonal Data Collector... Goodbye!!")