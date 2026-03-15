'''#subscripting
print("hello"[0])#subscripting 
print("hello"[4])
print("hello"[-1])#using negative indexin counting backwards from the end of the string

#string
print("123" + "123")#print the 2 strings together

#Integer = whole number
print(123+123)#add the 2 numbers

#Large Integers
print(123_456_789)#using _ to simulate he , between numbers

#Float= floating point number
print(3.1416)#print the float point number

#Boolean
print(True)
print(False)
'''

'''#type checking give you the data types
print(type("Hello"))
print(type(123))
print(type(123_456.78))
print(type(True))

#type casting or type conversion
print(int("123") + int("456"))#convert the string into a integer type and add the two numbers
#print(int("abc") + int("456"))#This line give you a value error

print("number of letters in your name: " + str(len(input("Enter your name"))))
'''

'''#Mathematical operations
print("my age: " + str(12))
print(123+456)#add
print(123-456)#substraction
print(123*456)#multiplication
print(123/456)#division
print(5//3)#division give you a whole number without decimal places
print(2**3)#power of a number

#PEMDAS = Parentheses,Exponent, multiplication/Division, Addition/Substraction
print(3*3+3/3-3)

#Rounding
number= 3.141618
print(round(number))#round to a whole number
print(round(number,2))#round to 2 decimal places

#Assigment operator +=,-=,*=,/=

score=0
score+=1
print(score)

#f-strings
a=0
h=1.8
to_win=True
print(f"A = {a}, h is {h}. so is {to_win}")
'''

print("Welcome to the tip Calculator!")
bill=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
final_amount= round(bill_with_tip, 2)
print(f"Each person should pay: ${final_amount}")

