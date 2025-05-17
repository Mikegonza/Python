'''
species_1 = "Sandhill Crane"
count_1 = 550
region_1 = "Midwest"
species_2 = "Blackpoll Warbler"
count_2 = 700
region_2 = "Southwest"

THRESHOLD = 500

#The use of the and operator does ensure that both conditions must be true for the result to be true, which is crucial for our logic.
species_1_high = region_1 != "Midwest" and count_1 > THRESHOLD# YOUR CODE HERE
species_2_high = region_2 != "Midwest" and count_2 > THRESHOLD# YOUR CODE HERE
print(f"Unusual pattern for {species_1}: {species_1_high}")
print(f"Unusual pattern for {species_2}: {species_2_high}")

# Expected output:
# Unusual pattern for Sandhill Crane: False
# Unusual pattern for Blackpoll Warbler: True
'''
'''def c_to_f():
    # FIXME
    return  temp_f# FIXME: Finish

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

# FIXME: Call conversion function
temp_f = temp_c * (9/5) + 32

# FIXME: Print result
print('Fahrenheit:' , temp_f)
'''
'''
def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

max_sum = (find_max(num_a,num_b)+(find_max(num_y,num_z)))

print('max_sum is:', max_sum)
'''
'''
def calc_base_area(base_length, base_width):
   return base_length * base_width

def calc_pyramid_volume(base_length, base_width, pyramid_height):
   return (calc_base_area(base_length,base_width)*pyramid_height)*(1/3)
   

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')
'''
'''
def get_user_num():
   print('FIXME: Finish get_user_num()')
   return -1

def compute_avg(user_num1,user_num2):
      print('FIXME: Finish compute_avg()')
      return-1

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)
'''
'''
def calc_ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and 
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('eBay fee: $', calc_ebay_fee(selling_price))

'''

size = 5

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:')

def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:')

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
