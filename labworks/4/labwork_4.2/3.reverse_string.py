word = input("Enter a string = ")

def reverse(word):
    if word == "":
        return ""
    return reverse(word[1:]) + word[0]

print("Reverse string:", reverse(word))