# List with various data types
various_data_types = [
    516,
    112.49,
    True,
    "meow",
    ("Western", "Governors", "University"),
    {"apple": 1, "pear": 5}
]

# Read index input from the user
index = int(input())

# Get the type name of the element at the input index
element_type = type(various_data_types[index]).__name__

# Print output in required format
print(f"Element {index}: {element_type}")
