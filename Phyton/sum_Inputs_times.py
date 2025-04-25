# Read 5 integer inputs
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# Create a list of inputs
values = [a, b, c, d, e]

# Integer sum
int_sum = sum(values)

# Float sum
float_sum = sum(float(x) for x in values)

# String concatenation
string_sum = ''.join(str(x) for x in values)

# Print results
print(f"Integer: {int_sum}")
print(f"Float: {float_sum}")
print(f"String: {string_sum}")
