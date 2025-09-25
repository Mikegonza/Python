'''print("Welcome to the rollercoster!")
height=int(input("What is your heigth in cm? "))

if height >= 120:
    print("You can ride the rollercoster")
else:
    print("Sorry you have to grow taller before you can ride")
'''

'''number=int(input("What is the number you wnat to check? "))
if number%2==0:
    print("Even")
else:
    print("odd")
'''

''' if,elif,else statements
print("Welcome to the rollercoster!")
height=int(input("What is your heigth in cm? "))

if height >= 120:
    print("You can ride the rollercoster")
    age=int(input("What is your age? "))
    if age <= 12:
        print("Please pay 5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride")
'''

'''BMI if statement
weight = 63
height = 1.85

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5:
    print("normal weight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
'''

'''Multiple if statements
print("Welcome to the rollercoster!")
height=int(input("What is your heigth in cm? "))
bill=0

if height >= 120:
    print("You can ride the rollercoster")
    age=int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Child tickets are $5.")
    elif age <= 18:
        bill=7
        print("Youth tickets are $7.")
    else:
        bill=12
        print("Adult tickets are $12.")
    wants_photo = input("Do you wnat to have a photo take? Type y for Yes and n for NO. " )
    if wants_photo =="y":
        #add $3 to their bill
        bill+=3

    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride")
'''  

'''Pizza selection
print("Welcome to pizza deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra chesse? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
bill=0
if size=="S" or "s":
    bill+=15
elif size=="M" or "m":
    bill+=20
elif size=="L" or "l":
    bill+=25
else:
    print("You typed the wrong inputs.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

# todo: work out their final amount based on wheather if they want extra chesse.
if extra_cheese=="Y":
    bill+=1

print(f"Your final bill is: ${bill}.")

'''

