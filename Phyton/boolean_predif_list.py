# Predefined list
predef_list = [4, -27, 15, 33, -10]

# Read user input
user_input = int(input())

# Compare input to maximum value in list
is_greater = user_input > max(predef_list)

# Print result in specified format
print(f"Greater Than Max? {is_greater}")