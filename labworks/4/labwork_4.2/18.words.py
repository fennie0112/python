def divide_words(words):
    vowels = []
    consonants = []

    for word in words:
        if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
            vowels.append(word)
        else:
            consonants.append(word)

    return vowels, consonants

words = ["apple", "ball", "orange", "cat", "umbrella"]

v, c = divide_words(words)

print("Vowel words =", v)
print("Consonant words =", c)