def checkzero(nums):
    # Taking numbers from the user.
    for i in range(nums):
        numbers = int(input(f"Enter number {i+1}: "))
        number_list.append(numbers)
    # print(number_list)

    new_list = [] # New list to store all numbers converted into string.
    for values in number_list:
        str_value = str(values)
        new_list.append(str_value)
    print(new_list)

number_list = [] # List to store all user input numbers.
n = int(input("Enter total numbers: "))
checkzero(n)