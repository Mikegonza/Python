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

