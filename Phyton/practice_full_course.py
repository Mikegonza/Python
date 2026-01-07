''' #Print statement
#https://www.youtube.com/watch?v=rfscVS0vtbw&t=5055s&ab_channel=freeCodeCamp.org 
print("hello world!")
print("    *")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("\n")
#Print statement 
character_name = "Miguel"
character_age = "40"
print("There was a man named " + character_name + ", ")
#updating the same variable 
character_name = "For his last name"
print("He was "+ character_age + " years old. ")
print("but did not like beign " + character_age + ".")
print("but did not like call " + character_name + ".")
#Strings \n next character to a new line.
#\ escape character to include a " or ' in the text
#creating a variable string
phrase = "Type:\n"
#concatanation with + sign
print(phrase + "World\n\'wide\n\'web")
#using functions
phrase = "live long and prosper:"
print(phrase.lower())
print(phrase.islower())
print(phrase.upper())
print(phrase.isupper())
#get the length of a string start from 0
print(len(phrase))
#get the value of first character
print(phrase[0])
#get the index value of "g"
print(phrase.index("g"))
#get the index of "long" giving the value of where the word start in the phrase
print(phrase.index("and"))
#replace a value in the phrase
print(phrase.replace("prosper","travel"))
#types of numbers
print(100)
print(2.0)
print(-2)
print(2 + 2)
print(5 - 2)
print(2 * 2)
print(10 / 2)
print(10 % 3)# modulus operator its going to print the remainder of the operation 
#store a value in a variable
mynum= 10
print(mynum)
#covert number into a string
print(str(mynum))
#print strings with numbers
print(str(mynum)+" numbers are fun.")
# math functions abs(absolute value)
my_num=-5
print(abs(my_num))
# pow function to get the power of a number
print(pow(3,2))
# max return the bigger number
print(max(6,10))
# min return the smallest number
print(min(6,10))
# round (round a decimal number)
print(round(6.6))
print(round(6.5))

#import math functions
from math import *
# floor round the number down not mater the number after decimal point
print(floor(3.7))
# ceil round the number up not mater the number after decimal point
print(ceil(3.7))
#print the square root of a number
print(sqrt(36))

#get input from a user
name = input("Enter your name: ")
age= input("Enter your age: ")
print("Hello " + name + "!" + " " +"You are "+ age + " " + "years old")

# Basic calculator
num1= input("Enter a number: ")
num2= input("Enter another number: ")
#using int function and convert num1 and num2 strings into numbers
whole_number = int(num1) + int(num2)
print(whole_number)
#using float function to work with decimal numbers
decimal_num1= input("Enter decimal number: ")
decimal_num2= input("Enter another decimal number: ")
decimal = float(decimal_num1) + float(decimal_num2)
print(decimal)

#creating a madlibs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''
''' #List
friends= ["kevin","Karen","Luis","Nicole","Jacqueline"]
#index      0       1        2      3         4
print(friends)
print(friends[0])# print the first element of the list
print(friends[4])# print the last element of the list
print(friends[-1])# starts indexin from the back of the list
print(friends[1:])# print elements from the especific index number
print(friends[1:3])# print elements from the specific index but not including the second index parameter
friends[1]="Mike"#replace a value inside of the list
print(friends[1])#print the replace value
'''
''' #List functions
lucky_numbers=[4,8,42,23,16,15]
winners= ["kevin","Karen","Luis","Nicole","Jacqueline"]
winners.sort() # (sort)put it in alphabetical order
lucky_numbers.sort() #order number in ascending order
lucky_numbers.reverse()#reverse the order of the list
lucky_numbers2=lucky_numbers.copy() #copy the exact same list from another list
print(lucky_numbers2)
print(winners)

winners.extend(lucky_numbers) # add list togehter
print(winners)

winners.append("Jose") #add a element at the end of the list
print(winners)

winners.insert(1,"Jose") # add an element between elements pushing to the rigth from the specific index
print(winners)

winners.remove("Nicole") # remove an element 
print(winners)

winners.pop() # remove the last element of the list 
print(winners)

print(winners.index("Luis")) # obtain the index value of a element
print(winners.count("Jose")) # count how many times the same value shows in the list

winners.clear() # remove all elements from the a list giving an empty list
print(winners)
'''
''' tuple and funcions
#tuple we cannot change the value and use () , list use [] and the values ares mutables
coordinates= (4,5)
print(coordinates[0])

#functions
def say_hi():                    #define a function
    print("this is a function!")
print("this is the top")        #example of indentation in a function
say_hi()                         #calling the function
print("this is the bottom")     #indentation

def parameter_function(name,age):  #Giving parameters to a function
    print("hello " + name + " you are " + str(age)) #body of the function converting integer into a string value
parameter_function("Mike",40)     #calling a function and giving the parameter, note:second parameter is a integer
parameter_function("Nicole",10)
'''
''' #Return statement
def cube(num):
    return num*num*num
result= cube(4)
print(result)
'''
'''# if statement and comparisons 
is_male = True #boolean value
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("You are neither male nor tall")
#Comparisons operator
def max_num(num1,num2,num3):
    if num1>=num2 and num1>= num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3 
print(max_num(300,40,5))
'''
'''# Advance Calculator with if statements
num1= float(input("Enter firts number: "))
op= input("Enter operator (+,-,/,*): ")
num2= float(input("Enter second number: "))

if op=="+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")
'''
'''#Dictionaries with strings and integers
month_Translator_English_To_Spanish={
    "January": "Enero",
    "February": "Febrero",
    "March":"Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre"
}
print(month_Translator_English_To_Spanish["January"])
print(month_Translator_English_To_Spanish.get("February"))
print(month_Translator_English_To_Spanish.get("Other"))#for key that is not on the dictionary giving back a none result
print(month_Translator_English_To_Spanish.get("Other","Not a valid key"))#for key that is not on the dictionary
#Dictionaries using integers
month_Number={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
print("The name for the number of the month you entered is:",month_Number[2])
'''
'''#while loops
i= 1        #initialize the variable
while i<=10:#define the condition for the loop
    print(i)#action to execute the loop
    i+=1    #iteration check for the condition
print("Done with the loop!")#last line after the final iteration of the loop
'''
'''#Guessing game
password="password"
guess_password=""
guess_count=0
guess_limit=3
out_Of_Guess=False

while guess_password!=password and not (out_Of_Guess):
    if guess_count < guess_limit:
        guess_password=input("Enter the password:")
        guess_count+=1
    else:
        out_Of_Guess=True
if out_Of_Guess:
    print("Sorry not more chances to guess!")
else:
    print("Yay, you guess the password!")
'''
'''#for loop
for letter in "Python is awesome": #print each letter in the string including spaces
    print(letter)
    
pets=["Dog","Cat","Bird"]
for pet in pets: #print each element of the array of strings
    print(pet)

brands=["Polo","Adidas","Bose"]
for index in range(len(brands)): #print each element of the array of strings
    print(brands[index])
    
for index in range(5):#print each number from 0 to 5, not including 5
    print(index)

for index in range(3,10):#print each number from 3 to 10, not including 10
    print(index)
    
for index in range(5):#printing and pointing the first iteartion 
    if index==0:
        print("First Iteration")
    else:
        print("Not the first Iteration")
'''
'''#exponent function
def reaise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
print(reaise_to_power(2,3))
'''
'''#2D list and Nested loops
number_grid=[
#Col 0 1 2 
    [1,2,3],#Row0
    [4,5,6],#Row1
    [7,8,9],#Row2
    [0]     #Row3
]
print(number_grid[0][0])#print value from row0, column0
print(number_grid[2][1])#print value from row2, column1

for row in number_grid:#prints all elemnts 
    print(row)

for row in number_grid:#prints all elements individually
    for col in row:
        print(col)
'''
'''#Translation English to new language
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation + "G"
            else:
                translation=translation + "g"
        else:
            translation=translation +letter
    return translation
print(translate(input("Enter a phrase: ")))
'''
'''#Try Except
try:#user enter a value but if the value is not the same type is shows an error
    value=10/0
    number = int(input("Enter a number: "))#
    print(number)
except ZeroDivisionError as err: 
    print(err)#print out specific predifined error best practice
except:
    print("invalid input!")
'''
'''#Reading from files
#open("WordTextFile1.txt","r")#read only the info on the file
#open("WordTextFile1.txt","w")#writing in the file modifying content
#open("WordTextFile1.txt","a")#append add new information in the file
#open("WordTextFile1.txt","r+")#read and write on the file
example_file= open("WordTextFile1.txt","r")#passing the value to a variable to open a file with this structure
print(example_file.readable())#check if the file is available to read returning true if is available
print(example_file.read())#read and show the content if the file
print(example_file.readline())#read and show the firts line in the file(if we write two of thus consecutive we get an output line by line)
print(example_file.readlines())#read all the lines and put in a list
print(example_file.readline()[1])#shows the content for the firts line by the inex position(line) of the file
for example in example_file.readlines():#for loop to read a file
    print(example)
example_file.close()#close the file
'''
'''#Writting to files
#employee_file = open("F:\Python\Phyton\employees.txt", "r")
#print(employee_file.read())
#employee_file.close()

#employee_file = open("F:\Python\Phyton\employees.txt", "a")
#employee_file.write("Jose-new hiring")#append or add a new data at the end of the file
#employee_file.close()

#employee_file = open("F:\Python\Phyton\employees.txt", "a")
#employee_file.write("\nMarcos- Sales")#add a new value at the end of the file with a new line
#employee_file.close()

#employee_file = open("F:\Python\Phyton\employees.txt", "w")
#employee_file.write("\nJackie-Boss")#wirte a new value deleting everething else 
#employee_file.close()

#employee_file = open("F:\Python\Phyton\employees1.txt", "w")#create a new file if the name does not exist
#employee_file.write("\nMiguel-New Boss")
#employee_file.close()
'''
'''#modules
#import while_Loops #import the functionality of the program call while_loops
#print(while_Loops) #print the result of the function in while_loops program
'''
'''#classes and objects
#This is the class Student with the parameters to pass in to the attributes for objects
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
#This is the object to work in the Student Class assigning attributes
from Student import Student

student1= Student("Miguel", "Software Eng", 3.5, False)
student2= Student("Ramon", "System eng", 3.5, True)

print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)

print(student2.name)
print(student2.major)
print(student2.gpa)
print(student2.is_on_probation)
'''
'''#Multiple choise quiz 
# creating a module class(Question_main.py)
from Question import Question

question_prompts=[
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer= input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)

#creating a class question data type(Separate file Question.py)
class Question:
    def __init__(self, prompt, answer):
        self.prompt= prompt
        self.answer= answer
'''

'''#Functions with branches/ loops
def print_message(message):
    if len(message) > 6:
        print('too long')
    else:
        print(message)

print_message('How?')
print_message('How are you today?')

def compute(numbers):
    result = 0
    for num in numbers:
        result += num * 3
    return result

values = [7, 5, 6]
computed_value = compute(values)
print(computed_value)


def get_numbers():
    values = []
    for count in range(6):
        values.append(int(input()))
    return values

def print_selected_numbers():
    numbers = get_numbers()
    for number in numbers:
        if (number % 3) != 0:
            print(number)

print_selected_numbers()

def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        bag_ounces= bag_ounces * 6

user_ounces = int(input())
print_popcorn_time(user_ounces)

'''

'''#problem1
#Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small". 
# If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by " seconds".
#Sample output with input: 7   
# 42 seconds

def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        print(str(6 * bag_ounces) +" seconds")

user_ounces = int(input())
print_popcorn_time(user_ounces)
'''

'''#problem2
#Write a function print_shampoo_instructions() with parameter num_cycles. 
# If num_cycles is less than 1, print "Too few.". If more than 4, print "Too many.". 
# Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done."
#Sample output with input: 2
#1 : Lather and rinse.
#2 : Lather and rinse.
#Done.
def print_shampoo_instructions(num_cycles):
    if num_cycles<1:
        print("Too few.")
    elif num_cycles>4:
        print("Too many.")
    else:
        for i in range(1, num_cycles + 1):
            print(f"{i} : Lather and rinse.")
        print("Done.")

user_cycles = int(input())
print_shampoo_instructions(user_cycles)
'''

'''#Functions can be passed as arguments.
def print_human_head():
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return

def print_monkey_head():
    print('   .-"-.')
    print(' _/.-.-.\\_')
    print('( ( o o ) )')
    print(' |/  "  \\|')
    print('  \\ .-. /')
    print('  /`"""`\\')
    return

def print_figure(face):
    face()  # Print the face
    print('     |')
    print('   --|--')
    print('  /  |  \\')
    print('@    |    @')
    print('     |')
    print('    /|\\')
    print('   @   @')
    return

choice = int(input('Enter "1" to draw monkey, "2" for human: '))

if choice == 1:
    print_figure(print_monkey_head)
elif choice == 2:
    print_figure(print_human_head)
'''

'''#List argument modification.
#Address the FIXME comments. Move the respective code from the while-loop to the created function.
#The add_grade function has already been created.
#Note: split() and strip() are string methods further explained elsewhere. 
#split() separates a string into tokens using any whitespace as the default separator. 
#The tokens are returned in a list (i.e., 'a b c'.split() returns ['a', 'b', 'c']). 
#strip() returns a copy of a string with leading and trailing whitespace removed.

def add_grade(student_grades):
    print('Entering grade. \n')
    name, grade = input(grade_prompt).split()
    student_grades[name] = grade

# FIXME: Create delete_name function
def delete_name():
    print('Deleting grade.\n')
    name = input(delete_prompt)
    del student_grades[name]

# FIXME: Create print_grades function
def print_grades():
    print('Printing grades.\n')
    for name, grade in student_grades.items():
            print(name, 'has a', grade)

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
delete_prompt = "Enter name to delete:\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

command = input(menu_prompt).lower().strip()

while command != '4':  # Exit when user enters '4'
    if command == '1':
        add_grade(student_grades)
    elif command == '2':
        # FIXME: Only call delete_name() here
        delete_name()        
        
    elif command == '3':
        # FIXME: Only call print_grades() here
        print_grades()
        
    else:
        print('Unrecognized command.\n')

    command = input().lower().strip()
'''

'''swap elements
#Write a function swap that swaps the first and last elements of a list argument.

#Sample output with input: 'all,good,things,must,end,here'
#['here', 'good', 'things', 'must', 'end', 'all']
def swap(lst):
    lst=lst[-1]
    print(lst)
    print(lst[0:])


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
'''

'''rounding and math
# import math
# help(math.pow)  # Display the documentation for the math module
# help(math)  # Display the documentation for the math module

# "rounding"
# num=3.14159
# print("%.2f" % num)  # Format the number to 2 decimal places
# print("{:.3f}".format(num))  # Another way to format the number to 3 decimal places
# print("{}".format(round(num, 4)))  # Round the number to 4 decimal places

'''

'''#Raw string
my_string = "This is a \n \"normal\" string\n"
my_raw_string = r"This is a \n \"raw\" string"

print(my_string)
print(my_raw_string)
'''

'''#Flor division
user_num = int(input())
div_num = int(input())

user_num = user_num//div_num
print(user_num,end=' ')
user_num = user_num//div_num
print(user_num,end=' ')
user_num = user_num//div_num
print(user_num,end=' ')
'''

'''# Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368
age = int(input())
weight = float(input())
heart_rate = float(input())
time = float(input())

calories = (((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781 - 75.4991)) * time)/8.368

print(f"Calories: {calories:.2f} calories")
'''

'''#math functions 
import math

x = float(input())
y = float(input())
z = float(input())

your_value1 = (math.pow(x,z))
your_value2 = (math.pow(x,(math.pow(y,z))))
your_value3 = (abs(x-y))
your_value4 = (math.sqrt(math.pow(x,z)))

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')
'''
'''#more math functions
import math

# Read the initial frequency
f0 = float(input())

# Compute r = 2^(1/12)
r = math.pow(2, 1/12)

# Compute and print the frequencies
print(f'{f0:.2f} Hz')
print(f'{f0 * (math.pow(r,1)):.2f} Hz')
print(f'{f0 * (math.pow(r,2)):.2f} Hz')
print(f'{f0 * (math.pow(r,3)):.2f} Hz')
'''

'''#string basics1
fav_fruit='jujube'
least_fav_fruit = input()

print('My favorite fruit',fav_fruit,'has',len(fav_fruit),'characters')
print('My least favorite fruit',least_fav_fruit,'has',len(least_fav_fruit),'characters')
'''

'''#string basics2
fav_drink = input()
print('The last character of',fav_drink,'is',fav_drink[-1])
'''

'''#string basics3 concatenation

student_name = input()
course_name = input()

student_courses_str = student_name + ' is studying ' + course_name

print(student_courses_str)
'''

'''#list 1
#Program to calculate statistics from student test scores.
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(f'{num_midterm_scores} students took the midterm.')
print(f'{num_final_scores} students took the final.')

#Calculate the number of students who took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(f'{dropped_students} students must have dropped the class.')

lowest_final = min(final_scores)
highest_final = max(final_scores)

print(f'\nFinal scores ranged from {lowest_final} to {highest_final}')

# Calculate the average midterm and final scores
# Hint: Sum the midterm scores and divide by number of midterm takers
#       Repeat for the final
average_midterm = sum(midterm_scores)/(num_midterm_scores)
print(average_midterm)

average_final_score = sum(final_scores)/(num_final_scores)
print(average_final_score)

print(all_scores)
print(len(all_scores))
print(sum(midterm_scores))
print(dropped_students)
print(num_midterm_scores)

'''

'''#list 2
#List names_list is created with two names read from input. Then, list countries_list is created with two countries read from input.
#  On one line, output:names_list's first element ,' lives in ',countries_list's second element,a period ('.')
# Reads two values from input into names_list
names_list = [input(), input()]
# Reads two values from input into countries_list
countries_list = [input(), input()]

print(names_list[0], 'lives in', countries_list[1] + '.')
'''

'''#list 3
#List countries_list is created with the first three countries read from input. 
# Remove the second element of countries_list.
# Then, read an additional country from input and append the country to countries_list.

# Reads three values from input into countries_list
countries_list = [input(), input(), input()]
print(countries_list)

countries_list.pop(1)
read_countries_list=input()
countries_list.append(read_countries_list)

print(countries_list)
'''

'''#List 4
#List days_list is created with four integers read from input. 
# Using list methods and/or functions, assign:

#len_var with the length of days_list.
#index_var with the index of the element 6 in days_list.
#max_var with the largest element of days_list.
# Reads four values from input into days_list
days_list = [int(input()), int(input()), int(input()), int(input())]

len_var = len(days_list)
index_var=days_list.index(6)
max_var= max(days_list)

print(f'List length: {len_var}')
print(f'6 is found at index {index_var} of {days_list}')
print(f'Max: {max_var}')
'''

'''#List basics 4.1 extra practice
#Given the user inputs, complete a program that does the following tasks:

#Define a list, my_list, containing the user inputs: my_flower1, my_flower2, and my_flower3 in the same order.
#Define a list, your_list, containing the user inputs, your_flower1 and your_flower2, in the same order.
#Define a list, our_list, by concatenating my_list and your_list.
#Append the user input, their_flower, to the end of our_list.
#Replace my_flower2 in our_list with their_flower.
#Remove the first occurrence of their_flower from our_list without using index().
#Remove the second element of our_list.
#Observe the output of each print statement carefully to understand what was done by each task of the program.
my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()

their_flower = input()

# 1. TODO: Define my_list containing my_flower1, my_flower2, and my_flower3
# in that order
my_list=[my_flower1,my_flower2,my_flower3]
# 2. TODO: Define your_list containing your_flower1 and your_flower2
# in that order
your_list=[your_flower1,your_flower2]
# 3. TODO: Define our_list by concatenating my_list and your_list
our_list= my_list + your_list
print(our_list)

# 4. TODO: Append their_flower to the end of our_list
our_list.append(their_flower)
print(our_list)

# 5. TODO: Replace my_flower2 in our_list with their_flower
our_list.remove(my_flower2)
our_list.insert(1,their_flower)
print(our_list)

# 6. TODO: Remove the first occurrence of their_flower from
#our_list without using index()
our_list.pop(1)
print(our_list)

# 7. TODO: Remove the second element of our_list
our_list.pop(1)
print(our_list)
'''

'''#Tuple
#Create a new variable point that is a tuple containing the strings 'X string' and 'Y string'.
point = ('X string','Y string')

white_house_coordinates = (38.8977, 77.0366)
print(f'Coordinates: {white_house_coordinates}')
print(f'Tuple length: {len(white_house_coordinates)}')

# Access tuples via index
print(f'\nLatitude: {white_house_coordinates[0]} north')
print(f'Longitude: {white_house_coordinates[1]} west\n')

# Error. Tuples are immutable
#white_house_coordinates[1] = 50

'''

'''#named tuples
from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car

print(chevy_blazer)
print(chevy_impala)

#Create a new named tuple Dog that has the attributes name, breed, and color.
Dog = namedtuple('Dog', ['name', 'breed', 'color'])

#Let 
Address = namedtuple('Address', ['street', 'city', 'country']) 
# Create a new address object house where house.street is "221B Baker Street", house.city is "London", and house.country is "England".
house = Address('221B Baker Street', 'London', 'England')

#Given the following named tuple Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats']), 
# and data objects car1 and car2, write an expression that computes the sum of the price of both cars.
#car1.price + car2.price
'''

'''#tuple 1
#School is a named tuple with fields: name, city, state, and enrollment. 
# Variable school_data is a School object created with three strings and one integer read from input as attributes. 
# Output the following:
# "School name: " followed by school_data's name attribute
#"City: " followed by school_data's city attribute
#"State: " followed by school_data's state attribute
#"Enrollment: " followed by school_data's enrollment attribute
from collections import namedtuple

School = namedtuple('School', ['name', 'city', 'state', 'enrollment'])

school_data = School(input(), input(), input(), int(input()))

print(f'School name:',school_data[0])
print(f'City:',school_data[1])
print(f'State:',school_data[2])
print(f'Enrollment:',school_data[3])
'''

'''#tuple 2
#Three values are read from input and are stored into variables city_name, state_located, and population_count.
# Initialize a tuple named city_data to store city_name, state_located, and population_count, in that order.
city_name = input()
state_located = input()
population_count = int(input())

city_data = (city_name,state_located,population_count)

print(f'City name: {city_data[0]}, State: {city_data[1]}, Population: {city_data[2]}')
'''

'''#tuple 3
#Import the namedtuple container from collections. 
# Then, define a named tuple called Person with fields: first_name, last_name, and license_plate, in that order.
from collections import namedtuple
Person = namedtuple('Person',['first_name','last_name','license_plate'])

first_name = input()
last_name = input()
license_plate = input()

person = Person(first_name, last_name, license_plate)

print(f'First name: {person.first_name}, Last name: {person.last_name}, License plate: {person.license_plate}')
'''

'''#tuple 4
#City is a named tuple with fields: name, state, and population. Read two strings and one integer from input. 
# Create city_data as a City tuple, and initialize city_data with city_name, state_located, and population_count as the fields.
from collections import namedtuple

City = namedtuple('City', ['name', 'state', 'population'])

city_name=input()
state_located=input()
population_count=int(input())

city_data= City( city_name, state_located,population_count)

print(f'City name: {city_data.name}, State: {city_data.state}, Population: {city_data.population}')
'''

'''#Set basics 1
#List names_list contains three strings read from input. Create a set named unique_names containing the unique strings in names_list.
names_list = [input(), input(), input()]

unique_names= set(names_list)

print(sorted(unique_names))
'''

'''#set basics 2
#An integer is read from input into variable new_number. 
#Add new_number to numbers_picked. Then, assign num_numbers with the number of elements in numbers_picked.
numbers_picked = {16, 20, 34}

new_number = int(input())

numbers_picked.add(new_number)
num_numbers=len(numbers_picked)

print(sorted(numbers_picked))
print(f'Number of values picked: {num_numbers}')
'''

'''#set basics 3
#Set animals_set1 contains 'stork'. Set animals_set2 contains two strings read from input. Perform the following tasks:
#Read the next string from input and add the string to animals_set1.
#Update animals_set1 with animals_set2.
#Remove one random element from animals_set2.

animals_set1 = {'stork'}
animals_set2 = set()
animals_set2.add(input())
animals_set2.add(input())

animals_set1.add(input())
animals_set1.update(animals_set2)
animals_set2.pop()

print(f'animals_set1: {sorted(animals_set1)}')
print(f'animals_set2 size: {len(animals_set2)}')
'''

'''#set basics 4
#Set my_favorites contains 'goat', 'horse', and 'penguin'. 
#Set your_favorites contains three strings read from input. 
#Assign likeable_animals with the union of my_favorites and your_favorites.

my_favorites = {'goat', 'horse', 'penguin'}
your_favorites = {input(), input(), input()}

my_favorites=set(my_favorites)
your_favorites=set(your_favorites)
likeable_animals=my_favorites.union(your_favorites)

print(f'My favorite animals: {sorted(my_favorites)}')
print(f'Your favorite animals: {sorted(your_favorites)}')
print(f'Likeable animals: {sorted(likeable_animals)}')
'''

'''#set basics 4.1 extra practice
#Given the user inputs, complete a program that does the following tasks:
#Define a set, fruits, containing the user inputs: my_fruit1, my_fruit2, and my_fruit3.
#Add the user inputs, your_fruit1 and your_fruit2, to fruits.
#Add the user input, their_fruit, to fruits.
#Add your_fruit1 to fruits.
#Remove my_fruit1 from fruits.
#Observe the output of each print statement carefully to understand what was done by each task of the program.
#Note: For testing purposes, sets are printed using sorted() for comparison, as in the book's examples.
my_fruit1 = input()
my_fruit2 = input()
my_fruit3 = input()

your_fruit1 = input()
your_fruit2 = input()

their_fruit = input()

# 1. TODO: Define a set, fruits, containing my_fruit1, my_fruit2, and my_fruit3
fruits={my_fruit1,my_fruit2,my_fruit3}
print(sorted(fruits))

# 2. TODO: Add your_fruit1 and your_fruit2 to fruits
fruits.add(your_fruit1)
fruits.add(your_fruit2)

print(sorted(fruits))

# 3. TODO: Add their_fruit to fruits
fruits.add(their_fruit)

print(sorted(fruits))

# 4. TODO: Add your_fruit1 to fruits
fruits.add(your_fruit1)
print(sorted(fruits))

# 5. TODO: Remove my_fruit1 from fruits
fruits.remove(my_fruit1)
print(sorted(fruits))
'''

'''#Dictionary basics
#Two string and integer pairs are read from input,
#  each pair representing a student's name and score on a test.
#  Complete the following steps:

#Create an empty dictionary named scores_dict.
#Add the following two key-value pairs to the dictionary named scores_dict:
#Key student_name1 with the value person_score1
#Key student_name2 with the value person_score2
student_name1 = input()
person_score1 = int(input())
student_name2 = input()
person_score2 = int(input())

scores_dict={}
scores_dict[student_name1]=person_score1
scores_dict[student_name2]=person_score2

print(f'{student_name1}: {scores_dict[student_name1]}')
print(f'{student_name2}: {scores_dict[student_name2]}')
'''

'''#Dictionary basics 2
#Dictionary contact_dict contains three key-value pairs,
#  each representing an authentication code sent to an email address. 
# An integer is read from input into variable key_name, 
# representing an authentication code in contact_dict. Complete the following steps:

#Output the email address corresponding to key_name in dictionary contact_dict.
#Delete the key-value pair associated with key_name from contact_dict.
contact_dict = {365558: 'Dax@mushrooms.org', 112264: 'Jen@enchiladas.org', 846292: 'Mia@cookies.com'}
key_name = int(input())

print(contact_dict[key_name])
del contact_dict[key_name]

print('Remaining pairs:')
print(contact_dict)
'''

'''#dictionary basics 3
#Dictionary test_scores contains four key-value pairs each representing a student's name and score on a test. Complete the following steps:
#Read a string from input into variable key_name, representing a student's name.
#Modify the test score associated with key_name so that the updated value is the original value minus 4.
test_scores = {'Mel': 65, 'Meg': 30, 'Abe': 67, 'Mai': 71}
print('Original:')
print(test_scores)

key_name=input()
test_scores[key_name]=test_scores[key_name]-4

print('Updated:')
print(test_scores)
'''

'''#Dictionary basics 4
#Three integers are read from input into variables meeting1, meeting2, and meeting3. Complete the following steps:

#Create an empty dictionary named important_dates.
#Add the following three key-value pairs to the dictionary named important_dates:
#Key 'August' with the value meeting1
#Key 'March' with the value meeting2
#Key 'February' with the value meeting3

meeting1 = int(input())
meeting2 = int(input())
meeting3 = int(input())

important_dates={}
important_dates['August']=meeting1
important_dates['March']=meeting2
important_dates['February']=meeting3

print(f"August: {important_dates['August']}")
print(f"March: {important_dates['March']}")
print(f"February: {important_dates['February']}")
'''

'''#Dictionary basics 5
#Dictionary food_quantities contains four key-value pairs, each representing a food name and the quantity ordered.
#  A string is read from input into variable key_name, representing a food name in food_quantities. Complete the following steps:

#Output the quantity corresponding to key_name in dictionary food_quantities.
#Delete the key-value pair associated with key_name from food_quantities.

food_quantities = {'muffins': 45, 'waffles': 74, 'tacos': 55, 'avocados': 30}
key_name = input()

print(food_quantities[key_name])
del food_quantities[key_name]

print('Remaining pairs:')
print(food_quantities)
'''

'''Dictionary basics 6
#Dictionary age_dict contains four key-value pairs each representing a student's name and age. Complete the following steps:
#Read a string from input into variable key_name, representing a student's name.
#Modify the age associated with key_name so that the updated value is the original value plus 3.

age_dict = {'Tia': 47, 'Noa': 39, 'Fay': 44, 'Del': 14}
print('Original:')
print(age_dict)

key_name=input()
age_dict[key_name]=age_dict[key_name]+3

print('Updated:')
print(age_dict)
'''

'''#Dictionary basics 7
#Dictionary time_to_word contains twelve key-value pairs. Complete the following steps:
#Read integers timeA and timeB from input, representing an event's start and end times.
#Use time_to_word to output key timeA's value followed by ' to ' and key timeB's value.
time_to_word = {
	1: 'one', 2: 'two', 3: 'three', 4: 'four',
	5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
	9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'
}

timeA=int(input())
timeB=int(input())
print(time_to_word[timeA],'to',time_to_word[timeB])
'''

'''#Extra practice
#1.-Calculates the overall grade for four equally weighted programming assignments, in which each assignment is graded out of 50 points.
# Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).

#2.-Calculates the overall grade for four equally weighted programming assignments, in which assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.

#3.-Calculates the overall grade for a course with three equally weighted exams (graded out of 100 points)
# that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50 points)
# that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.

exam1_grade = float(input("Enter score on Exam 1 (out of 50): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 50): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 50): "))
exam4_grade = float(input("Enter score on Exam 4 (out of 50): "))

exam1_grade = exam1_grade/50
exam2_grade = exam2_grade/50
exam3_grade = exam3_grade/50
exam4_grade = exam4_grade/50

overall_grade = (exam1_grade + exam2_grade + exam3_grade + exam4_grade) / 4 *100

print(f"Your overall grade is: {overall_grade}")
'''

'''#Types of conversions
input_text = input('Enter a number:\n')
float_variable = float(input_text)
int_variable = int(float_variable)

print(f'original input text: {input_text}')
print(f'input text converted to a float: {float_variable}')
print(f'float variable converted to an int: {int_variable}')
'''

'''#Types conversions 1
#An integer is read from input into variable num_feet. 
# Use a conversion function to convert the value of num_feet to a string and assign the value to the variable str_feet.
num_feet = int(input())

num_feet=str(num_feet)
str_feet= num_feet

print('Number of feet: ' + str_feet)
'''

'''#Types conversion 2
#Given that 1 dollar = 100 cents, 
# complete the multiplication of num_dollars and CENTS_PER_DOLLAR so that the result is implicitly converted to a float.
CENTS_PER_DOLLAR = 100
num_dollars = float(input())

num_cents = float(num_dollars)* CENTS_PER_DOLLAR

print(f'{num_cents} cents')
'''

'''#Types conversions 3
#Two integers are read from input into variables num_kilometers1 and num_kilometers2. 
# Assign avg_kilometers_per_hour with the average kilometers per hour. Then, convert avg_kilometers_per_hour to an integer.
num_kilometers1 = int(input())
num_kilometers2 = int(input())

avg_kilometers_per_hour= (num_kilometers1 + num_kilometers2)/2
avg_kilometers_per_hour= int(avg_kilometers_per_hour)

print(avg_kilometers_per_hour)
'''

'''#Binary numbers
#Set each binary digit for the unsigned binary number below to 1 or 0 to obtain the decimal equivalents of 9, then 50,
#  then 212, then 255. Note that 255 is the largest integer that the 8 bits can represent.

# 1   2   4   8   16   32   64   128
# 2⁰  2¹  2²  2³  2⁴   2⁵   2⁶   2⁷

'''

'''#(f-String) formatted string literals
#first_name and last_name are read from input. Modify the f-string f'{}, {}' so that:
#The first {} contains last_name.
#The second {} contains first_name.
first_name = input()
last_name = input()
print(f'{last_name}, {last_name}')
'''

'''#(f-String) formatted string literals 1
#x is read from input as an integer, representing the side length of a square. 
# Compute the square's area as x*x. Use f-string's = sign feature within the provided 
# curly brackets as the replacement field to output both the expression and result.
x = int(input())

print(f'{x*x=}')
'''

'''#(f-String) formatted string literals 2
#input_num is read from input as a floating-point value. Using format specifications, output the following:
#input_num in exponent notation
#input_num in fixed-point notation with six places of precision
input_num = float(input())

print(f'{input_num:e}')
print(f'{input_num:.6f}')
'''

'''#string formatting (simple statistics) extra practice
# Given 4 floating-point numbers. 
# Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.
#Output each rounded integer using the following:
#print(f'{your_value:.0f}')
#Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
#print(f'{your_value:.3f}')
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

your_value=num1*num2*num3*num4
print(f'{your_value:.0f}',end=" ")
your_value=(num1+num2+num3+num4)/4
print(f'{your_value:.0f}')

your_value=num1*num2*num3*num4
print(f'{your_value:.3f}',end=" ")
your_value=(num1+num2+num3+num4)/4
print(f'{your_value:.3f}')
'''

'''#if-else statement
user_num = int(input("Enter a number: "))

div_remainder = user_num % 2

if div_remainder == 0:
    print(f"{user_num} is even.")
else:
    print(f"{user_num} is odd.")
'''

'''#elif statement 1
num_cards = int(input())

if num_cards == 24:
    print('Euchre')
elif num_cards == 36:
    print('Short deck')
else:
    print('Another deck size')
'''

'''#elif statement 2
#If num_players is:
#1, output 'Solo'.
#5, output 'Quintet'.
#6, output 'Sextet'.
#Otherwise, output 'Another number of musicians'.
num_players = int(input())

if num_players == 1:
    print('Solo')
elif num_players == 5:
    print('Quintet')
elif num_players == 6:
    print('Sextet')
else:
    print('Another number of musicians')
'''

'''#Detecting ranges with branches(operator chaining)
#Variable user_grade is read from input. Use operator chaining to complete the if-else expression as follows:
#If the value of user_grade is between 9 and 12 (both inclusive), then 'in high school' is output.
#Otherwise, 'not in high school' is output.
#Ex 1: If the input is 10, then the output is:
#in high school
#Ex 2: If the input is 8, then the output is:
#not in high school
#Note: 0 < x < 5 evaluates to true if x is between the ranges 0 and 5 (both non-inclusive).
user_grade = int(input())

if 12>user_grade>9:
    print('in high school')
else:
    print('not in high school')
'''

'''#Detecting ranges with branches 
#When the input variable number_of_bicycles is:
#greater than or equal to 49, output 'Need multiple racks'.
#between 12 inclusive and 49 exclusive, output 'Large bike rack'.
#between 0 exclusive and 11 inclusive, output 'Single bike rack'.
#less than or equal to 0, output 'Invalid input'.
number_of_bicycles = int(input())

if number_of_bicycles >= 49:
    print('Need multiple racks')
elif 49 > number_of_bicycles >=12:
    print('Large bike rack')
elif 11 >= number_of_bicycles > 0:
    print('Single bike rack')
elif number_of_bicycles <= 0:
    print('Invalid input')
'''

'''#Detecting ranges using logical operators.
#Modify the given if statement so that 'Not a mid-size town' is output if population_input is outside the range 1000 - 4650 inclusive.
population_input = int(input())

if (population_input < 1000) or (population_input > 4650):
    print('Not a mid-size town')
else:
    print('Mid-size town')
'''

'''#Detecting ranges using logical operators 2
#The 32% tax bracket applies to input_pay in the range 53000 - 85000 inclusive. 
#Write an if statement that outputs '32% tax bracket' 
# if the input input_pay is in this range. Otherwise, output 'Different tax bracket'.
input_pay = int(input())

if (input_pay >= 53000) and (input_pay <=85000):
    print('32% tax bracket')
else:
    print('Different tax bracket')
'''

'''#Detecting ranges using logical operators 3
#The temperature of lead in degrees Fahrenheit is read from input into variable lead_temp. If lead_temp is:
#≤ 621 degrees Fahrenheit, output 'The lead is now a solid.'
#> 621 degrees Fahrenheit and < 3164 degrees Fahrenheit, output 'The lead is now a liquid.'
#Otherwise, output 'The lead is now a gas.'
lead_temp = int(input())

if lead_temp <= 621:
    print('The lead is now a solid.')
elif (lead_temp > 621) and (lead_temp < 3164):
    print( 'The lead is now a liquid.')
else:
    print( 'The lead is now a gas.')
'''

'''#Detecting ranges using logical operators 4
# If year_input is in the inclusive range:
#1950 - 1959, output 'The 50s'.
#1960 - 1969, output 'The 60s'.
#1970 - 1979, output 'The 70s'.
#Otherwise, output 'Not in the period of research'.
year_input = int(input())

if (year_input >= 1950) and (year_input <= 1959):
    print('The 50s')
elif (year_input >= 1960) and (year_input <= 1969):
    print('The 60s')
elif (year_input >= 1970) and (year_input <= 1979):
    print('The 70s')
else:
    print('Not in the period of research')
'''

'''# Ranges with gaps.
#Integer mushrooms_available is read from input representing the number of mushrooms. Output 'Unreasonable batch' if:
#the number of mushrooms is fewer than 15.
#or the number of mushrooms is 30 or more.
mushrooms_available = int(input())
if (mushrooms_available < 15) or (mushrooms_available >= 30):
    print('Unreasonable batch')
'''

'''#Ranges with gaps 2
#Float length_kilometers is read from input representing a length in kilometers. 
# If the length is shorter than 40.5 kilometers or longer than 90.5 kilometers, output 'Discard'. 
# Otherwise, output 'Approve'.
length_kilometers = float(input())
if (length_kilometers < 40.5) or (length_kilometers > 90.5):
    print('Discard')
else:
    print('Approve')
'''

'''#Range with gaps 3
#Integer berries_count is read from input representing the number of berries. Output:
#'Small carton', if there are 20 - 70 berries inclusive.
#'Medium carton', if there are 110 - 160 berries inclusive.
berries_count = int(input())
if (70 >= berries_count >= 20):
    print('Small carton')
elif (160 >= berries_count >= 110):
    print('Medium carton')
'''

'''#Range with gaps 4
#Integer num_forks is read from input representing the number of forks. Output:
#'Standard bin', if the number of forks is greater than or equal to 30 and less than or equal to 70.
#'Full bin', if the number of forks is greater than 130 and less than or equal to 170.
#'Not efficient to ship', otherwise.
num_forks = int(input())
if (num_forks >= 30) and (num_forks <= 70):
    print('Standard bin')
elif (num_forks > 130) and (num_forks <= 170):
    print('Full bin')
else:
    print('Not efficient to ship')
'''

'''#Detecting multiple features with branches.
#car_year is read from input. Write multiple if statements:
#If car_year is 1953 or later, output 'Probably can carry several people.'
#If car_year is 1962 or earlier, output 'Probably only has a few safety features.'
#If car_year is after 1991, then output 'Probably has traction control.'
car_year = int(input())
if car_year >= 1953:
    print('Probably can carry several people.')
if car_year <= 1962:
    print('Probably only has a few safety features.')
if car_year > 1991:
    print('Probably has traction control.')
'''

'''#Detecting multiple features with branches. 2
#input_num1 and input_num2 are read from input. Write one if statement and one if-else statement:
#If input_num1 is less than or equal to 30, then output 'input_num1 is less than or equal to 30.'
#If input_num2 is greater than 5, then assign input_num2 with 10.
#Otherwise, output 'input_num2 is less than or equal to 5.'
input_num1 = int(input())
input_num2 = int(input())

if input_num1 <= 30:
    print('input_num1 is less than or equal to 30.')
if input_num2 > 5:
        input_num2 = 10
else:
    print('input_num2 is less than or equal to 5.')

print(f'input_num2 is {input_num2}.')
'''

'''#Detecting multiple features with branches 3
#Integers num_pizzas and my_cash are read from input. Each pizza costs 15 dollars.
#Write the following if-else statement. Within the else branch, write the following assignment and nested if-else statement:
#If num_pizzas is less than 3, output 'Not enough pizzas purchased'.
#Otherwise:
#Assign variable total_cost with the product of num_pizzas and 15.
#If total_cost is less than or equal to my_cash, then output 'Approved transaction'.
#Otherwise, output 'Not all pizzas purchased'.
num_pizzas = int(input())
my_cash = int(input())
if num_pizzas < 3:
    print('Not enough pizzas purchased')
else:
    total_cost= num_pizzas * 15
    if total_cost <= my_cash:
        print('Approved transaction')
    else:
        print('Not all pizzas purchased')
'''

'''#Membership operators: in/not in
# Use the "in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print(f'Found {name} on the roster.')
else:
    print(f'Could not find {name} on the roster.')
#///////////////////////////////////////////////////
# Use the "not in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name not in barcelona_fc_roster:
    print(f'Could not find {name} on the roster.')
else:
    print(f'Found {name} on the roster.')
#///////////////////////////////////////////////////
'''

'''#Identity operators: is/is not
w = 500
x = 500 + 500  # Create a new object with value 1000
y = w + w      # Create a second object with value 1000
z = x          # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('z and y are NOT bound to the same object')
'''

'''#Boolean operators: Detect specific values.
#Write an expression using membership operators that prints "Special number"
#if special_num is one of the special numbers stored in the list special_list = [-99, 0, 44].
#Sample output with input: 17
#Not special number
special_list = [-99, 0, 44]
special_num = int(input())

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')
'''

'''#Conditional expression: Print negative or nonnegative.
#Create a conditional expression that evaluates to string "negative" if user_val is less than 0, and "nonnegative" otherwise.
#Sample output with input: -9
#-9 is negative
user_val = int(input())

cond_str = "negative" if(user_val<0) else "nonnegative"

print(f'{user_val} is {cond_str}')
'''

'''#Conditional expression: Conditional assignment.
#Using a conditional expression, write a statement that increments num_users if update_direction is 3, 
#otherwise decrements num_users.
#Sample output with inputs: 8 3
#New value is: 9
num_users = int(input())
update_direction = int(input())

num_users = num_users+1 if(update_direction==3) else num_users-1

print(f'New value is: {num_users}')
'''

'''#Golf scores record the number of strokes used to get the ball in the hole.
#The expected number of strokes varies from hole to hole and is called par (possible values: 3, 4, or 5). 
#Each score's name is based on the actual strokes taken compared to par:
#"Eagle": number of strokes is two less than par
#"Birdie": number of strokes is one less than par
#"Par": number of strokes equals par
#"Bogey": number of strokes is one more than par
#Given two integers that represent the number of strokes used and par, 
#write a program that prints the appropriate score name. 
#Print "Error" at the end of the output if par is not 3, 4, or 5, or if the score's name is not "Eagle", "Birdie", "Par", or "Bogey".
strokes = int(input())
par = int(input())

score_name = ""

# Check for valid par
if par not in (3, 4, 5):
    score_name = "Error"
else:
    diff = strokes - par
    if diff == -2:
        score_name = "Eagle"
    elif diff == -1:
        score_name = "Birdie"
    elif diff == 0:
        score_name = "Par"
    elif diff == 1:
        score_name = "Bogey"
    else:
        score_name = "Error"

print(f"Par {par} in {strokes} strokes is {score_name}")
'''

'''#Leap year
#A year in the modern Gregorian Calendar consists of 365 days. 
# In reality, the earth takes longer to rotate around the sun. 
# To account for the difference in time, every 4 years, a leap year takes place. 
# A leap year is when a year has 366 days: An extra day, February 29th. 
# The requirements for a given year to be a leap year are:
#1) The year must be divisible by 4
#2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400; therefore, both 1700 and 1800 are not leap years
#Some example leap years are 1600, 1712, and 2016.
#Write a program that takes in a year and determines whether that year is a leap year.
is_leap_year = False   
input_year = int(input())

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    is_leap_year = True

# Print result based on is_leap_year
if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")
'''

'''#Primary U.S. interstate highways are numbered 1-99. 
# Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. 

# Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits.
# Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

#Given a highway number, indicate whether it is a primary or auxiliary highway. 
# If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.
#invalid
highway_number = int(input())
if ((highway_number < 1 or highway_number > 999) or (highway_number % 100 == 0)):
    print(f"{highway_number} is not a valid interstate highway number.")
#valid
else:
    if(highway_number>99):
        print(f"I-{highway_number} is auxiliary", end='')
        #get the primary
        primary_number = highway_number % 100 #get the rigthmost 2 digits
        print(f", serving I-{primary_number}",end='')
    else:
        primary_number = highway_number
        print(f"I-{primary_number} is primary", end='')
    #directions
    if (primary_number % 2 == 0):
        print(", going east/west.")
    else:#odd
        print(", going north/south.")
'''

'''#while loops examples
#A while loop is a construct that repeatedly executes an indented block of code (known as the loop body) 
# as long as the loop's expression is True. At the end of the loop body, 
# execution goes back to the while loop statement and the loop expression is evaluated again. 
# If the loop expression is True, the loop body is executed again. But, 
# if the expression evaluates to False, then execution instead proceeds to below the loop body.
# Each execution of the loop body is called an iteration, and looping is also called iterating.
#Assume user would enter 'a', then 'b', then 'n'.
# Get character from user here
user_char=input()
while user_char != 'n':
    print(f'character {user_char} is not the same')
    user_char=input()# Get character from user here
'''

'''#While loop with a sentinel value
#While loop example: Face-printing program that ends when user enters 'q'.
nose = '0'  # Looks a little like a nose

# Get first character for eyes and mouth
user_input = input("Enter a character ('q' for quit): ")
user_value = user_input[0]

# Loop until user enters sentinel value
while user_value != 'q':
    print(f' {user_value} {user_value} ')  # Print eyes     
    print(f'  {nose}  ')  # Print nose     
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): ")
    user_value = user_input[0]

print('Goodbye.\n')
'''

'''#While loop iterations.
x = 1
y = 3
z = 5
while (not (y < x < z)):
    print(x, end=' ')
    x = x + 1
#infinite loop
x = 10
while x != 3:
    print(x, end=' ')
    x = x / 2
'''

'''#Integer user_input is read from input. Write a while loop that reads values from input and 
# casts the values into integers, while a negative integer is read. In each iteration:
#Update sum_ints with the sum of sum_ints and user_input.
#Then, read the next integer from input into variable user_input.
sum_ints = 0
user_input = int(input())

while user_input < 0:
    sum_ints = sum_ints + user_input
    user_input = int(input())

print(sum_ints)
'''

'''#Integer user_num is read from input. Write a while loop that iterates while user_num is non-negative. In each iteration:
#Update value output_num as follows:
#If user_num is divisible by 3, output 'miss' and do not update output_num.
#Otherwise, output 'hit' and increment output_num.
#Then, read the next integer from input into variable user_num.
output_num = 0
user_num = int(input())

while user_num >= 0:
    if user_num  % 3==0:
        print('miss')
    else:
        print('hit')
        output_num += 1
    user_num = int(input())

print(f'Output number is {output_num}')
'''

'''#Greatest common divisor
num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print(f'GCD is {num_a}') 
'''

'''#while loop: Conversation 
#Program that has a conversation with the user.
#Uses elif branching and a random number to mix up the program's responses.
#import random  # Import a library to generate random numbers

print('Tell me something about yourself.')
print('You can type \'Goodbye\' at anytime to quit.\n')

user_text = input()

while user_text != 'Goodbye':
    random_num = random.randint(0, 2)  # Gives a random integer between 0 and 2
    if random_num == 0:
        print('\nPlease explain further.\n')
    elif random_num == 1:
        print(f'\nWhy do you say: "{user_text}"?\n')
    elif random_num == 2:
        print('\nWhat else can you share?\n')
    else:
        print('\nUh-oh, something went wrong. Try again.\n')

    user_text = input()

print('It was nice talking with you. Goodbye.\n')
'''

'''#while minimum
entered_value = int(input())

minimum_number = entered_value

while entered_value > 0:
    if entered_value < minimum_number:
        minimum_number = entered_value
    entered_value = int(input())

print(f'Min value: {minimum_number}')
'''

'''#while product
final_product = 1
entered_value = int(input())

while entered_value > 0:
    final_product = final_product * entered_value
    entered_value = int(input())

print(f'Product: {final_product}')
'''

'''#while Discount
user_age = int(input())

while (user_age < 15 or user_age > 70):
    if user_age < 15:
        print('5% discount')
    else:
        print('15% discount')
    user_age = int(input())

print('Regular ticket price')
'''

'''#while keep bidding
import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()
'''

'''#while double
num_insects = int(input())

""" Your solution goes here """
while num_insects <= 100:
    print(num_insects)
    num_insects = num_insects * 2
'''

'''#while input not equal
expected_string = input()
input_string = input()

word_count = 1

while input_string != 'Stop':
    if input_string == expected_string:
        word_count+=1
    input_string= input()

print(f'{expected_string} occurs {word_count} time(s).')
'''

'''#while input between
input_item = input()
furniture_number = int(input())

while 20 <= furniture_number <= 45:
    input_item = input()
    furniture_number = int(input())

print(f'{input_item}: is out of range!')
'''

'''#while current data less than previuos data
previous_data = int(input())
current_data = int(input())
print(f'Sequence starts at {previous_data}.')

while current_data < previous_data:
    print(f'{current_data} is less than {previous_data}. Sequence is decreasing.')
    previous_data = current_data
    current_data= int(input())
'''

'''#while Counting with a while loop
#Program that calculates savings and interest

initial_savings = 10000
interest_rate = 0.05

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(f' Savings at beginning of year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')
'''

'''#while Loop over presidential election years.
year = 1792
current_year = 2025

while year <= current_year:
    # Print the election year
    print(year)
    year = year + 4
'''

'''#while Loop iterates over the odd integers from 1 to 9 (inclusive).
i = 1
while i <= 9:
    i=i+2# Loop body statements go here

#Loop iterates over the odd integers from 211 down to 31 (inclusive).
i = 211
while i >= 31:
    i= i-2# Loop body statements go here
    
#Loop iterates from -100 to 65.
i=-100
while i <= 65:
    # Loop body statements go here
    i = i + 1
'''

'''#while Integer num_threshold is read from input. Initialize variable k with 7. Then, 
#write a while loop to perform the following tasks at each iteration until k is greater than num_threshold:
#Output the value of k.
#Increase k by 5.
num_threshold = int(input())

k=7
while k <= num_threshold:
    print(k)
    k = k+5
'''

'''#for loop: Looping over strings, lists, and dictionaries.
cities = {
    'Paris': 958,
    'Toronto': 550,
    'Nairobi': 309,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)'''

'''#for loop: Integer in_count is read from input representing the number of values to be read next. 
#The remaining values are read from input into paint_list. For each value in paint_list, 
#output the value followed by ' selected' on the same line.
in_count = int(input())
paint_list = []

for i in range(in_count):
    paint_list.append(input())

print(f'List has {in_count} elements:')

for paint in paint_list:
    print(f'{paint} selected')'''

'''#for loop: Integer val_count is read from input representing the number of values to be read next. 
#The remaining values are read from input into member_list. 
# Use a for loop to output all values in member_list in reverse order on the same line, 
# and surround each value with angle brackets '<' and '>'. After the loop terminates, output a newline.
val_count = int(input())
member_list = []

for i in range(val_count):
    member_list.append(input())

print(f'List has {val_count} elements:')

for member in reversed(member_list):
    print(f'<{member}>', end='')

print()'''

'''#for loop: student_dict is a dictionary with students' name and height pairs. A new student is read from input and added into student_dict.
#For each student in student_dict, output the student's name, followed by "'s height: ", and the student's height. 
#Then, assign average_value with the average of all the heights in student_dict.
student_dict = {
    'Sid': 141,
    'Ken': 177,
    'Lei': 194,
    'Mae': 174,
    'Avi': 182
}

name = input()
height_cm = int(input())
student_dict[name] = height_cm

total_height = 0

for name in student_dict:
    print(f"{name}'s height: {student_dict[name]}")
    total_height += student_dict[name]

average_value = total_height / len(student_dict)

print(f'Average height: {average_value:.2f}')'''

'''#Counting using the range() function
#Every integer from 0 to 500.
#range(501)
#Every integer from 10 to 20
#range(10,21)
#Every 2nd integer from 10 to 20
#range(10,21,2)
#Every integer from 5 down to -5
#range(5,-6,-1)
#i starts with 0. Each iteration outputs the value of i then decrements i by 1. 
#When i reaches -4, the loop body will not be entered because -4 > -4 is false.
#for i in range(0, -4, -1):
#    print(i, end=' ')'''

'''#range function: Positive integer hours_max is read from input, representing the hours since midnight. 
#Complete the range() function call so that the for loop iterates through the increasing sequence 
#of all non-negative integers less than or equal to hours_max.
hours_max = int(input())

print('Hours passed:', end=' ')

for i in range(0,hours_max+1):
    print(i, end=' ')
print()'''

'''#range function: Positive integers batch_begin and batch_end are read from input, 
#representing the batch numbers assigned to a collection of experimental data,with batch_begin less than batch_end. 
#Complete the for loop to iterate through the increasing sequence of all integers between batch_begin (inclusive) and batch_end (exclusive).
batch_begin = int(input())
batch_end = int(input())

print('Batch numbers:', end=' ')

for i in range(batch_begin,batch_end):
    print(i, end=' ')
print()'''

'''#range function: Integers start_time and end_time are read from input, 
# representing a range of time step of an activity. Complete the for loop as follows:
#Use curr_time as the loop variable.
#Iterate through the increasing sequence of all the integers from start_time to end_time, both inclusive, with a step of 5.
start_time = int(input())
end_time = int(input())

print('Time steps:', end=' ')

for curr_time in range(start_time,end_time+1,5):
    print(curr_time, end=' ')
print()'''

'''#range function: Integers start_month and stop_month are read from input, representing a period of time in months. 
#Integer start_month is less than stop_month. 
#For every other month between start_month and stop_month, both inclusive, 
#output 'Month picked: ' followed by each month's value.
start_month = int(input())
stop_month = int(input())

for month in range(start_month,stop_month+2,2):
    print(f'Month picked: {month}')'''

'''#Nested loop example: Histogram.
num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(num):
            print('*', end=' ')
        print('\n')

print('Goodbye.')
'''

'''#nested loop: 
c1 = 'a'
while c1 < 'b':
    c2 = 'a'
    while c2 <= 'c':
        print(f'{c1}{c2}', end = ' ')
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)
    #output:aa ab ac 
'''

'''#nested loop: 
i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}', end=' ')
        i2 = i2 + 3
    i1 = i1 + 10
    #output:13 16 19 113 116 119 
'''

'''nested loop
count = 0
for i in range(2):
   for j in range(4):
      count = count + 1
print(count)'''

'''#nested loop best example:
rows= int(input("enter the number of rows: "))
colums= int(input("enter the number of columns: "))
symbol= input("enter the symbol to use: ")

for x in range(rows):
    for y in range(colums):
        print(symbol,end="")
    print()'''

'''#nested loop: characters
letter1 = 'e'
while letter1 < 'g':
    letter2 = 's'
    while letter2 <= 'u':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)'''

'''#nested loop excersice
#Integers num_rows and num_columns are read from input representing the number of rows and columns of a theater's seating plan. 
#Complete the nested for loop to output each seat label, as shown in the example. 
#Each seat label is followed by a space, and each row is followed by a newline.
#Define the outer for loop with no indentation to iterate through each row of the theater. Use the loop variable current_row and iterate num_rows times, starting with integer 1.
#In the outer loop's body, use one indentation to add a statement to initialize current_column_letter with 'A'.
#In the outer loop's body, define the inner for loop to iterate through each column of the theater. 
#Use the loop variable current_column and iterate num_columns times, starting with integer 1.
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of colums: "))

for current_row in range(1,num_rows+1):
    current_column_letter='A'
    for current_colum in range(1,num_columns+1):
        # Inner for loop statements
        print(f'{current_row}{current_column_letter}', end=' ')
        current_column_letter = chr(ord(current_column_letter) + 1)  # Used to increment letters
    print()'''

'''#nested loop 1
#Integers first_range and second_range are read from input. 
#The outer while loop executes first_range times. 
#Complete the inner while loop to execute (second_range + 1) times for each iteration of the outer while loop.
first_range = int(input())
second_range = int(input())

count = 0
i = 0
while i < first_range:
    j = 0
    while j<second_range+1:
        count += 1
        j += 1
    i += 1

print(f'Inner loop ran {count} times')'''

'''#nested loop 2
#Integers first_range and second_range are read from input. 
#The inner for loop executes (second_range + 1) times for each iteration of the outer for loop. 
#Complete the outer for loop to execute first_range times.
first_range = int(input())
second_range = int(input())

count = 0
for i in range(first_range):
    for j in range(second_range + 1):
        count += 1

print(f'Inner loop ran {count} times')'''

'''#nested loop 3
#Integers initial_value and final_value are read from input. 
#For each number from initial_value to final_value both inclusive, 
#output the number's value of dash characters ('-').
initial_value = int(input())
final_value = int(input())

for x in range(initial_value,final_value+1):
    print(x*'-')'''

'''#nested loop 4
#On Taj's farm, each plot of land is labeled with a letter followed by an integer.
#Given integers num_rows and num_columns, output the label for each plot of land, followed by a space. End each row with a newline.
#Rows are in alphabetical order. Plots of land in the first row all start with the letter A.
#Columns are in ascending order. Plots of land in the first column all end with the integer 1.
num_rows = int(input())
num_columns = int(input())
row_letter='A'

for row in range(1,num_rows+1):    
    for column in range(1,num_columns+1):
        print(f'{row_letter}{column}',end=' ')
    print()
    row_letter=chr(ord(row_letter)+1)
'''

'''#break and continue statements
threshold = int(input())

for a in range(0, 3):
    print(a + 1, end=": ")

    for b in range(0, 1):
        if a > threshold:
            print("_,", end="")
            continue

        print(b, end=",")

    print()
'''

'''#break and continue statements 1
#"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. 
# Create a for loop that compares each character of the two strings. For each matching character, add one point to user_score. 
# Upon a mismatch, end the loop.
#Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'

simon_pattern = input()
user_pattern = input()
user_score = 0

for i in range(len(simon_pattern)):
    if simon_pattern[i] == user_pattern[i]:
        user_score += 1
    else:
        break

print('User score:', user_score)
'''

'''#Getting both index and value when looping: enumerate()
#Integer num_applicants is read from input, representing the number of applicant names to be read from input. 
# List applicant_eligibilities contains the applicant names read from the remaining input. For each element in applicant_eligibilities, output:
#'Name: '
#the element
#', Position: '
#the element's index in the list plus one
num_applicants = int(input())

applicant_eligibilities = []
for i in range(num_applicants):
    applicant_eligibilities.append(input())

for (index,name) in enumerate(applicant_eligibilities):
    print(f'Name: {name}, Position: {index+1}')
'''

'''#Getting both index and value when looping: enumerate() 2
#Integer samples_count is read from input, representing the number of data samples to be read from input. 
#List values_list contains the data samples read from the remaining input. For each element in values_list:
#If the element is greater than or equal to 50, output 'Sample ' followed by the element's index in the list and ' needs attention'.
#Otherwise, output 'Sample ' followed by the element's index in the list and ' is ok'.
#Ex: If the input is:
#3
#50
#20
#90
#then the output is:
#Sample 0 needs attention
#Sample 1 is ok
#Sample 2 needs attention

samples_count = int(input())

values_list = []
for i in range(samples_count):
    values_list.append(int(input()))

for (index,value) in enumerate(values_list):
    if value >=50:
        print(f'Sample {index} needs attention')
    else:
        print(f'Sample {index} is ok')
'''

