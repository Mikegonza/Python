from pigAge import pigAge_converter

# Read input age
pig_years = int(input())

# Convert using the module function
human_years = pigAge_converter(pig_years)

# Print the result
print(f"{pig_years} is {human_years} in human years")
