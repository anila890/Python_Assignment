
def sort_dictionary(input_dict):
    
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict

user_input = input("Enter a dictionary (e.g., key1:value1, key2:value2): ")

input_dict = {}
for item in user_input.split(","):
    key, value = item.split(":")
    input_dict[key.strip()] = value.strip()

sorted_dict = sort_dictionary(input_dict)

print("Sorted Dictionary:", sorted_dict)