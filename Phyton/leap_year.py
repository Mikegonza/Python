# Initialize is_leap_year to False
is_leap_year = False

# Get the year as input
input_year = int(input())

# Check for leap year conditions
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    is_leap_year = True

# Print result based on is_leap_year
if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")
