
print("Welcome to the Interactive Personal Data Collector!", end="\n\n")

yourname = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print("Name:", yourname, "(Type:", type(yourname), ", Memory Address:", id(yourname), ")")
print("Age:", age, "(Type:", type(age), ", Memory Address:", id(age), ")")
print("Height:", height, "(Type:", type(height), ", Memory Address:", id(height), ")")
print("Favourite Number:", fav, "(Type:", type(fav), ", Memory Address:", id(fav), ")", end="\n\n")

print("Your birth year is approximately:", 2023 - age, "(based on your age of", age, ")\n")

print("Thank you for using the Personal Data Collector. Goodbye!")
