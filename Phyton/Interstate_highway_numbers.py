#Primary U.S. interstate highways are numbered 1-99. 
# Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. 

# Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits.
# Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

#Given a highway number, indicate whether it is a primary or auxiliary highway. 
# If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.
'''Solution 1
print('Enter a highway number:', end =' ')
highway_number = int(input())

odd_highway = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99]
even_highway = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98]
invalid_highway_number = [0,100,200,300,400,500,600,700,800,900]
odd = 'north/south'
even = 'east/west'

if highway_number in odd_highway:
    print(f'I-{highway_number} is primary, going north/south.')
elif highway_number in even_highway:
    print(f'I-{highway_number} is primary, going east/west.')
elif 100 <= highway_number <= 999 and highway_number % 100 not in invalid_highway_number:
    primary_number = highway_number % 100
    direction = 'north/south' if primary_number % 2 else 'east/west'
    print(f'I-{highway_number} is auxiliary, serving I-{primary_number}, going {direction}.')
elif highway_number in invalid_highway_number:
    print(f'{highway_number} is not a valid interstate highway number.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')

'''

'''#solution 2
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