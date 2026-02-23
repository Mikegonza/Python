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

'''#3
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
#list of mixed data elements
data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None, {"name": "John", "age": 25}]

#input for index
print("Enter index:")
index = int(input())

element = data_mixture[index]
data_type = type(element).__name__

# Determine category
if isinstance(element, (list, str, dict)):
    message = "This element is iterable."
elif isinstance(element, (int, float)):
    message = "This element is numeric."
else:
    message = "This is a different data type."

print(f"Element: {element}, Type: {data_type}, Message: {message}")
'''

'''#4
#Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by summing the two bases, multiplying the sum by the height, and then dividing by two.
#Trapezoid Area Formula:
#A = ((b1 + b2) * h) / 2
#The solution output should be in the format:
#Trapezoid area: area_value square meters
#Sample Input and Output:
#If the input is
#Enter base 1: 3
#Enter base 2: 4
#Enter height: 5
#then the expected output is
#Trapezoid area: 17.5 square meters
#Alternatively, if the input is
#Enter base 1: 3
#Enter base 2: 5
#Enter height: 7
#then the expected output is
#Trapezoid area: 28.0 square meters
print("Enter base 1:")
base_1 = int(input())

print("Enter base 2:")
base_2 = int(input())

print("Enter height:")
height = int(input())

# Calculate trapezoid area
area = ((base_1 + base_2) * height) / 2

# Output result
print(f"Trapezoid area: {area} square meters")
'''

'''#5
#Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type before finding the sum.

#First output: the sum of the five inputs as an integer value
#Second output: the sum of the five inputs after converting each input to a float value
#Third output: the concatenation of the five inputs after converting each input to a string
#The solution output should be in the format:
#Integer: integer_sum_value
#Float: float_sum_value
#String: string_sum_value
#Sample Input and Output:
#If the input is
#Enter 1st number:
#1
#Enter 2nd number:
#3
#Enter 3rd number:
#6
#Enter 4th number:
#2
#Enter 5th number:
#7
#then the expected output is
#Integer: 19
#Float: 19.0
#String: 13627
print("Enter 1st number:")
num1 = int(input())

print("Enter 2nd number:")
num2 = int(input())

print("Enter 3rd number:")
num3 = int(input())

print("Enter 4th number:")
num4 = int(input())

print("Enter 5th number:")
num5 = int(input())

# Integer sum
integer_sum = num1 + num2 + num3 + num4 + num5

# Float sum (convert each to float first)
float_sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)

# String concatenation
string_sum = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f"Integer: {integer_sum}")
print(f"Float: {float_sum}")
print(f"String: {string_sum}")
'''

'''#6
#Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.
#The solution output should be in the format:
#xxx-xx-xxxx
#Sample Input and Output:
#If the input is
#Enter Student Identification Number:
#123456789
#then the expected output is
#123-45-6789
#solution accepts a 9-digit integer representing an unformatted student identification number (e.g.,"5417543010")
#solution outputs formatted student identification number as a string (e.g.,"541-75-3010")
#accept integer input
print("Enter Student Identification Number:")
identification_number = input()
# Format using string slicing
formatted_id = identification_number[0:3] + "-" + identification_number[3:5] + "-" + identification_number[5:9]

print(formatted_id)
'''

'''#7
#Create a program that takes an integer input and determines whether it equals one of the values in this predefined list:
#predef_list = [4, -27, 15, 33, -10]
#Define a function named is_in_list() that outputs a Boolean value (True or False) based on whether the input value is present in predef_list.
#The solution should produce the output in the following format:
#True if the input is in the list, otherwise False.
#Is the input present in the list? Boolean_value
#Sample Input and Output:
#If the input is
#20
#then the expected output is
#Is the input present in the list? False
#Alternatively, if the input is
#33
#then the expected output is
#Is the input present in the list? True
predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating whether integer input is in predef_list

#accept integer input
print("Enter the number to check for in the list:")
user_input = int(input())

#define function to compare input with list values
def is_in_list(value):
    return value in predef_list



#output desired statement based on is_in_list() function
if __name__ == '__main__':
    result = is_in_list(user_input)
    print(f"Is the input present in the list? {result}")
'''

'''#8
#Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
#frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
#Output the string element of the index value entered. Place the solution in a try block and implement an exception of "Error" if an incompatible integer input is provided.
#The solution output should be in the format:
#frameworks_element
#Sample Input and Output:
#If the integer input is
#2
#then the expected output is
#CherryPy
#Alternatively, if the integer input is
#7
#then the expected output is
#Error
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

#try-block to determine value
try:
  print("Enter the index of the element that you want to extract from the list:")  
  index = int(input()) #accept integer input
  print(frameworks[index])          

except:
    print("Error")
'''

'''#9
#Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:
#If the temperature is below 33° F, the water is “Frozen”.
#If the water is between 33° F and 80° F (including 33°), the water is “Cold”.
#If the water is between 80° F and 115° F (including 80°), the water is "Warm".
#If the water is between 115° F and 211° F (including 115°) , the water is “Hot".
#If the water is greater than or equal to 212° F, the water is “Boiling”.
#Additionally, output a safety comment only during the following circumstances:
#If the water is exactly 212° F, the safety comment is, "Caution: Hot!"
#If the water temperature is less than 33° F, the safety comment is, "Watch out for ice!"
#The solution output should be in the format:
#water_state
#optional_safety_comment
#Sample Input and Output:
#If the input is
#Enter the water temperature:
#118
#then the expected output is
#Hot
#Alternatively, if the input is
#Enter the water temperature:
#32
#then the expected output is
#Frozen
#Watch out for ice!
#temperature >= 212, water state is "Boiling"
#temperature (115, 211], water state is "Hot"
#temperature [80, 115], water state is "Warm"
#temperature [33, 80), water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution accepts integer input representing a water temperature
#solution outputs the water state and potential safety comment based on temperature

print("Enter the water temperature:")
temperature = int(input())

#determine water state and safety comment
if temperature < 33:
    print("Frozen")
    print("Watch out for ice!")
elif temperature < 80:
    print("Cold")
elif temperature < 115:
    print("Warm")
elif temperature < 212:
    print("Hot")
elif temperature == 212:
    print("Boiling")
    print("Caution: Hot!")
else:
    print("Boiling")
'''

'''#10
#Create a solution that accepts an integer input identifying how many different shares of stock are purchased from the Old Town Stock Exchange, 
# followed by an equivalent number of string inputs representing the stock selections. 
#The following dictionary, stock, lists available stock selections as the key and the cost per selection as the value.
#stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
#Output the total cost of the purchased shares of stock to two decimal places.
#The solution output should be in the format:
#Total price: $cost_of_stocks
#Sample Input and Output:
#If the input is
#Enter a quantity of stocks followed by stock symbol(s):
#3
#SOFI
#AMZN
#LVLU
#then the expected output is
#Total price: $150.53
#Alternatively, if the input is
#Enter a quantity of stocks followed by stock symbol(s):
#2
#KIRK
#TSLA
#then the expected output is
#Total price: $921.58
stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

# input 
print("Enter a quantity of stocks followed by stock symbol(s):")
num_items = int(input())
total_cost = 0
# loop and calculations
for i in range(num_items):
    symbol = input()
    total_cost += stocks[symbol]

print(f"Total price: ${total_cost:.2f}")
'''

'''#11
#Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. The following dictionary purchase lists available items as the key and the cost per item as the value.

#purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
#Additionally,
#If fewer than 10 items are purchased, the price is the full cost per item.
#If between 10 and 20 items (inclusive) are purchased, the purchase gets a 5% discount.
#If 21 or more items are purchased, the purchase gets a 10% discount.
#Output the chosen item and the total purchase cost to two decimal places.
#The solution output should be in the format:
#quantity item_purchased total cost: $total_purchase_cost
#sample Input and Output:
#If the input is
#bananas
#12
#then the expected output is
#12 bananas total cost: $21.09
#Alternatively, if the input is
#cookies
#144
#then the expected output is
#144 cookies total cost: $585.79
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

print("Enter the item to purchase:")
item = input()
print("Enter the quantity of that item:")
quantity = int(input())
price_per_item = purchase[item]
total_cost = price_per_item * quantity

if quantity >= 21:
    total_cost *= 0.90
elif quantity >= 10:
    total_cost *= 0.95

print(f"{quantity} {item} total cost: ${total_cost:.2f}")
'''

'''#12
#Write a Python program that performs the following steps:

#Prompt the user to input the name of a text file (e.g., "WordTextFile.txt").
#The input file contains exactly three rows, each containing a single word.
#Using the open() function and the read() and write()methods, perform the following actions:
#Read the three words from the file.
#Construct a new sentence by combining these words in the same order, separating the words by spaces.
#Append this sentence to the end of the file on a new line.
#Display the updated contents of the file.
#Requirements:
#Use the open() function in the appropriate mode to read and write to the file.
#Ensure the words in the sentence are separated by a single space.
#Output the complete updated contents of the file, showing the original words followed by the newly appended sentence.
#Output Format:
#The program should print the updated file contents, with the original words on separate lines and the new sentence on a new line.
#Sample Input and Output:
#If the input is
#Enter the name of the input file:
#WordTextFile.txt
#Contents of WordTextFile.txt before the program runs:
#cat  
#chases  
#dog  
#then the expected output is
#cat  
#chases  
#dog  
#cat chases dog  
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence
#accept input identifying filename
print("Enter the name of the input file:")
filename = input()

#open, read, and write text file (e.g., "WordTextFile.txt") using open(), read(), write()
with open(filename, "r") as file:
    contents = file.read().strip()
    words = contents.split()

#open and write sentence to end of file
sentence = " ".join(words)

with open(filename, "a") as file:
    file.write("\n" + sentence)
 
#open, read, and output the updated file contents 
with open(filename, "r") as file:
    updated_contents = file.read()
    print(updated_contents)
'''

'''#13
#Write a Python program that performs the following steps:
#Prompt the user to input the name of a CSV file ("input1.csv").
#Use Python's built-in csv module to open and read the specified file.
#For each row in the file, reverse the order of elements (values separated by commas).
#Print the reversed elements for each row to the console.
#Requirements:
#Use the open() function to open the file.
#Use the csv.reader() method to read the file contents.
#Use a loop to iterate through each row and reverse the elements in the row.
#Print the reversed elements as a list for each row.
#Sample Input and Output:
#If the input is
#Enter the name of the file along with its extension:
#input1.csv  
#Contents of input1.csv:
#fruits,sports,countries
#banana,football,United States
#apple,soccer,Brazil
#orange,volleyball,Canada
#Then the expected output is
#['countries', 'sports', 'fruits']  
#['United States', 'football', 'banana']  
#['Brazil', 'soccer', 'apple']  
#['Canada', 'volleyball', 'orange']  
#Hints: Use Python's [::-1] slicing technique to reverse a list.
#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file ("input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements
import csv

#accept string input identifying filename
print("Enter the name of the file along with its extension:")
file_name = input()

#open, read, and output the new file contents in the reverse order
with open(file_name, 'r') as csvfile:
    reader= csv.reader(csvfile)
    
    for row in reader:
        reversed_row= row[::-1]
        print(reversed_row)      #open csv file
'''

'''#14
#Write a program that accepts two integer inputs from the user:
#A number for which the factorial will be calculated
#A number to compare the factorial result against
#Use the built-in math module and its factorial() function to compute the factorial of the first input number. Then, compare the computed factorial to the second input number and display the following:
#The factorial value of the first input
#A Boolean value indicating whether the factorial is greater than the second input
#The solution output should be in the format
#The factorial value of number is factorial_value
#Boolean_value
#Sample Input and Output:
#If the input is
#6
#500
#then the expected output is
#The factorial value of 6 is 720
#True
#Alternatively, if the input is
#4
#50
#then the expected output is
#The factorial value of 4 is 24
#False
#solution accepts integer input and integer comparison value
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is greater than identified comparison value

#import math module and call factorial()
import math

#accepts integer input
print("Enter a number to calculate its factorial:")
factorial_num = int(input())
print("Enter a number to compare with the factorial:")
comparison_num = int(input())

#factorial method
factorial_value= math.factorial(factorial_num)

#greater than user_input_comparison?
is_greater = factorial_value > comparison_num


#output factorial
print(f"The factorial value of {factorial_num} is {factorial_value}")
print(is_greater)
'''

'''#15
#Write a Python program that performs the following steps:
#Accept an integer input representing the age of a pig (in years).
#Import the pre-existing module pigAge.
#Use the built-in function pigAge_converter() from the module to calculate the human-equivalent age of the pig.
#Note: One year of a pig’s life is equivalent to five human years.
#Output the result in the given format where:
#input_pig_age is the pig's age in years.
#converted_pig_age is the human-equivalent age of the pig.
#The solution output should be in the format:
#input_pig_age pig years is equivalent to converted_pig_age in human years
#Sample Input and Output:
#If the input is
#8
#then the expected output is
#8 pig years is equivalent to 40 in human years
import pigAge

print("Enter the age of the pig in years:")
input_pigAge = int(input())

# Call the module function
converted_pig_age = pigAge.pigAge_converter(input_pigAge)

print(f"{input_pigAge} pig years is equivalent to {converted_pig_age} in human years")
'''
