#Write a program that takes a date as input and outputs the date's season in the northern hemisphere. 
# The input is a string to represent the month and an int to represent the day.

input_month = input()
input_day = int(input())

month_to_num = {'january': 1,'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
days_in_month = {'january':31,'february':28,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}

month = month_to_num.get(input_month.lower())
max_day = days_in_month.get(input_month.lower())

# Validate month and day
if month is None:
    print("Invalid")
elif not (1 <= input_day <= max_day):
    print("Invalid")
else:
    # Check season based on month and day
    if (month == 3 and input_day >= 20) or (month in [4, 5]) or (month == 6 and input_day <= 20):
        season = "Spring"
    elif (month == 6 and input_day >= 21) or (month in [7, 8]) or (month == 9 and input_day <= 21):
        season = "Summer"
    elif (month == 9 and input_day >= 22) or (month in [10, 11]) or (month == 12 and input_day <= 20):
        season = "Autumn"
    elif (month == 12 and input_day >= 21) or (month in [1, 2]) or (month == 3 and input_day <= 19):
        season = "Winter"
    else:
        season = "Invalid"

    # Print the season if everything is valid
    print(season)


