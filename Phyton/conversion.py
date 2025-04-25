# Read total ounces from input
total_ounces = int(input())

# Convert ounces to pounds and remaining ounces
total_pounds = total_ounces // 16
remaining_ounces = total_ounces % 16

# Convert pounds to tons and remaining pounds
tons = total_pounds // 2000
remaining_pounds = total_pounds % 2000

# Print output in required format
print(f"Tons: {tons}")
print(f"Pounds: {remaining_pounds}")
print(f"Ounces: {remaining_ounces}")
