#Calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
#Repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number 
#is less than 1. Hint: Use a while loop that will execute as long as num_rolls is greater than 1.
#Prints a histogram in which the total number of times the dice rolls equals each possible value is displayed by printing a character,
#  such as *, that number of times. The following provides an example:
#Dice roll histogram:
#2s:  **
#3s:  ****
#4s:  ***
#5s:  ********
#6s:  *************
#7s:  *****************
#8s:  *************
#9s:  *********
#10s: **********
#11s: *****
#12s: **

import random

while True:
    num_rolls = int(input("Enter number of times to roll the dice (less than 1 to quit): "))
    
    if num_rolls < 1:
        break

    # Initialize dictionary to count occurrences of sums from 2 to 12
    roll_counts = {i: 0 for i in range(2, 13)}
    
    # Simulate dice rolls
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        roll_counts[roll] += 1

    # Print histogram
    print("\nDice roll histogram:\n")
    for total in range(2, 13):
        print(f"{total}s: {'*' * roll_counts[total]}")
