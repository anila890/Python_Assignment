def has_unique_characters(input_string):
    
    input_string = input_string.replace(" ", "").lower()

    char_set = set()

    for char in input_string:
        if char in char_set:
            return False  
        char_set.add(char)

    return True  

input_string = input("Enter a string: ")

result = has_unique_characters(input_string)
print(result)