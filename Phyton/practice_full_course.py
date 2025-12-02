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


