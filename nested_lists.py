import random
import time

# Parameters: input(list)
# Return: flatten_array(list)
# Description: flatten a nested list of integers
# Creator: Bryce Egley
def flatten(input):
    flatten_array = []
    for i in input:
        if (isinstance(i, list)):
            flatten_array = flatten_array + flatten(i)
        else:
            flatten_array.append(i)
    return flatten_array

# Parameters: size(int)
# Return: new_array(list)
# Description: randomly generate a nested list of integers
# Creator: Bryce Egley
def build_nested_list(size):
    new_array = []
    for i in range(size):
        if random.randint(0,size) == 1:
            new_array.append(build_nested_list(size))
        else:
            new_array.append(random.randint(0,size))
    return new_array

# Parameters: none
# Return: user input(integer)
# Description: Get a integer from the user
# Creator: Bryce Egley
def input_number():
    try:
        return int(input("Enter the size of the randomly generated nested list: "))
    except:
        print("Please enter an integer")
        return input_number()

# Collect input from the user
user_input = input_number()
# Start the timer
start = time.time()
# Create the nested list
input = build_nested_list(user_input)
# Flatten the list
flatten_array = flatten(input)
# End the timer
end = time.time()
# Print results
print("Nested List of Integers")
print(input)
print("Flattened List of Integers")
print(flatten_array)
print("Time Elapsed: ")
print(end - start)
