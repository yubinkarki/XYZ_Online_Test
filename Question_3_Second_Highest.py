def second_high(num_list):
    highest = 0
    
    for i in num_list:
        if i > highest:
            highest = i
        
    return highest


num_list = [34, 1, 2, 33, 45, 56]
print(second_high(num_list))
