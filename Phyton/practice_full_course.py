'''
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
'''
#List
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

#List functions
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

























