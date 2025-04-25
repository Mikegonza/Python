import csv

# Read CSV filename from input
filename = input()

# List to store dictionaries
dicts = []

# Open and process the CSV
with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        # Create dictionary from alternating key-value elements
        row_dict = {row[i]: row[i + 1] for i in range(0, len(row), 2)}
        dicts.append(row_dict)

# Print the dictionaries
for d in dicts:
    print(d)
