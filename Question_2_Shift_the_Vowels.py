def string_vowels(name):
    name_char = []  # List for individual letters in the string.
    name_vowel = []  # List for vowels in the string.
    name_vowel_index = []  # List to store index of vowels from the name_char list.

    for i in name:  # Inserting all letters from string into list.
        name_char.append(i)
    print(name_char)


myinput = "Quickly"
print(string_vowels(myinput))
