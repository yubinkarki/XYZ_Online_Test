def encoder(text_to_encode):
    individual_letters = list(text_to_encode)  # Converting string and storing it as a list.
    unique_letters = []
    count_list = []
    new_count_list = []
    encoded_list = []

    # Getting unique letters from the string and storing it in a list.
    for x in individual_letters:
        if x not in unique_letters:
            unique_letters.append(x)
    # print(unique_letters)

    # Storing the number of occurrence of a letter in a list.
    for y in unique_letters:
        count_list.append(text_to_encode.count(y))
    # print(count_list)


myinput = "AAAAAaaaXMMMMMMMMMMMM"
print(encoder(myinput))
