text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)

if text == reverse:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")