text = input("Enter a string: ")

print(text.startswith("Hello")) 
print(text.endswith("World"))

print()

text = "Data123#Science!"

result = ""

for char in text:
    if char.isalpha():
        result = result + char

print(result)