#  my_str= 'http://en.wikipedia.org/wiki/Nasa/'
#   1-my_str[10:19],Returns the characters in indices 10-18.
#  print(f'1-',my_str[10:19])
#  2-my_str[10:-5],Returns the characters in indices 10-28.
#  print(f'2-',my_str[10:-5])
#  3-my_str[8:],Returns all characters from index 8 until the end of the string.
#  print(f'3-',my_str[8:])
#   4-my_str[:23],Returns every character up to index 23, but not including my_str[23].
#   print(f'4-',my_str[:23])
# 5-my_str[:-1],Returns all but the last character.
#   print(f'5-',my_str[:-1])
#       6-stride argument my_str[::]
#   print(f'6-',my_str[::])
#    7-stride argument my_str[::2] print every other character
#    print(f'7-',my_str[::2])
#    8-stride argument my_str[1:9:3] print every third character
#   print(f'8-',my_str[1:9:3])

#       start_index = int(input())
#       end_index = int(input())
#       my_string = 'Jack be nimble, Jack be quick'

#       ''' Your code goes here '''
#       my_str=my_string[start_index:end_index]
#       sliced_lyric=my_str

#       print('Full lyric:', my_string)
#       print('Sliced lyric:', sliced_lyric)


#      full_saying = input()

#      p_saying=full_saying[1:-1]
#      partial_saying=p_saying

#      print(partial_saying)

#     my_string = input()
#     sub_string=my_string[:3] + my_string[-2:]
#     print(sub_string)

#    full_string = input()

#    ''' Your code goes here '''
#    sub_lyric=full_string[len(full_string)//2:][::3]

#    print(sub_lyric)

#   print(f'{"Player Name":16}{"Goals":8}{"score":6}')

#   print('-' * 50)


#   print(f'{"Sadio Mane":16}{"22":8}{5:6}')

#   print(f'{"Gabriel Jesus":16}{"7":8}{6:6}')
#   print()

#  print(f'{5:4.1f}')
#  n = int(input("Enter a number: "))
#  count= 0
#  for i in range(2,n+1,2):
#    count=count+1
#    print(i)
#  print(count)
# n = int(input("enter a number: "))
# count=0
# for i in range(5,n+1,5):
#     count+=1
#  print(count)
# color_name = input()

# ''' Your code goes here '''
# print(f'{color_name:=^16}')
# print(f'{color_name:=>16}')

# location_size = float(input())

# ''' Your code goes here '''
# print(f'{location_size:.4f} acres')

# plants = input().split()
# planted = input().split()
# separator_char = input()

# ''' Your code goes here '''
# print(f'{"Plants":^18}|{"Planted":^18}')
# print(f'{separator_char*36:36}')
# print(f'{plants[0]:^18}|{planted[0]:^18}')
# print(f'{plants[1]:^18}|{planted[1]:^18}')
# print(f'{plants[2]:^18}|{planted[2]:^18}')

# word = 'onomatopoeia'
# num_guesses = 10

# hidden_word = '-' * len(word)

# guess = 1

# while guess <= num_guesses and '-' in hidden_word:
#     print(hidden_word)
#     user_input = input(f'Enter a character (guess #{guess}): ')
    
#     if len(user_input) == 1:
#         # Count the number of times the character occurs in the word
#         num_occurrences = word.count(user_input)
    
#         # Replace the appropriate position(s) in hidden_word with the actual character.
#         position = -1
#         for occurrence in range(num_occurrences):
#             position = word.find(user_input, position+1)  # Find the position of the next occurrence
#             hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]  # Rebuild the hidden word string
    
#         guess += 1
        
# if not '-' in hidden_word:
#     print('Winner!', end=' ')        
# else:
#     print('Loser!', end=' ')

# print(f'The word was {word}.')

# target = input()
# string_twister = input()

# """ Your code goes here """
# if target in string_twister:
#     print("Found at:",string_twister.find(target))
#     print(string_twister.replace(target,"--",2))
# else:
#     print("None found")

# superhero1 = input()
# superhero2 = input()

# """ Your code goes here """
# if superhero2 < superhero1:
#     print(superhero2)
# elif superhero1 < superhero2:
#     print(superhero1)
# else:
#     print("Same ASCII values")

# 

# user_entry = input()

# """ Your code goes here """
# user_entry = user_entry.strip()
# if "Course:" in user_entry:
#     user_entry = user_entry.lower()
# else:
#     user_entry = user_entry.capitalize()

# print(user_entry)