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

#Write a function swap that swaps the first and last elements of a list argument.

#Sample output with input: 'all,good,things,must,end,here'
#['here', 'good', 'things', 'must', 'end', 'all']
'''
def swap(lst):
    lst=lst[-1]
    print(lst)
    print(lst[0:])


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
'''

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
