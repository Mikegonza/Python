# Read 9-digit integer input
student_id = int(input())

# Ensure it's zero-padded to 9 digits
id_str = f"{student_id:09d}"

# Format as XXX-XX-XXXX
formatted_id = f"{id_str[:3]}-{id_str[3:5]}-{id_str[5:]}"

# Print result
print(formatted_id)
