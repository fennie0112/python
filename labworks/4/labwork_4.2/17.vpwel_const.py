def split_string(s):
    vowels = ""
    others = ""
    for ch in s:
        if ch.lower() in "aeiou":
            vowels = vowels + ch
        else:
            others = others + ch
    return vowels, others

s = input("Enter a string: ")
v, o = split_string(s)

print("Vowels =", v)
print("Other characters =", o)