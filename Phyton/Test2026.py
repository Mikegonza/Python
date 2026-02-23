'''#1
#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

#accept three integer inputs
print("Enter the number of days Employee A travels to job:")
employee_a = int(input())
print("Enter the number of days Employee B travels to job:")
employee_b = int(input())
print("Enter the number of days Employee C travels to job:")
employee_c = int(input())

# Distances per trip
distance_a = 15.62
distance_b = 41.85
distance_c = 32.67
#calculate total distance
total_miles = (employee_a * distance_a) + \
              (employee_b * distance_b) + \
              (employee_c * distance_c)

#output combined mileage
print(f"Distance: {total_miles:.2f} miles")
'''

'''#2
#Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the value of the input ounces. There are 16 ounces in a pound and 2,000 pounds in a ton.
#The solution output should be in the format:
#Tons: value_1
#Pounds: value_2
#Ounces: value_3
#If the input is
# 32500
# then the expected output is
# Tons: 1
# Pounds: 31
# Ounces: 4
#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

print("Enter the number of ounces to convert:")
ounces = int(input())

#convert ounces to pounds and tons 
# Convert ounces to pounds and remaining ounces
total_pounds = ounces // 16
remaining_ounces = ounces % 16

# Convert pounds to tons and remaining pounds
tons = total_pounds // 2000
remaining_pounds = total_pounds % 2000

#output number of tons, remaining pounds, and remaining ounces
print(f"Tons: {tons}")
print(f"Pounds: {remaining_pounds}")
print(f"Ounces: {remaining_ounces}")
'''

#3
#Create a solution that accepts an integer input representing the index value for any of the seven elements in the following list:
# data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None,{"name": "John", "age": 25}]
#The solution should perform the following:

#Retrieve the element at the given index.
#Determine its data type using the type() function and its .name attribute.
#Check if the element belongs to one of the following categories:
#If the element is "iterable" (e.g., list, str, dict), output, "This element is iterable."
#If the element is numeric (e.g., int, float), output, "This element is numeric."
#For other data types not in these categories, output, "This is a different data type."
#The solution output should be in the format:
#Element: [element_value], Type: [data_type], Message: [category_message]
#Sample Input and Output:
#If the input is
#Enter index:
#3
#then the expected out is
#Element: ['apple', 'banana', 'coconut'], Type: list, Message: This element is iterable.
#Alternatively, if the input is
#Enter index:
#1
#then the expected output is
#Element: 2024, Type: int, Message: This element is numeric.
