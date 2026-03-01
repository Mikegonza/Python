# # # # # my_str= 'http://en.wikipedia.org/wiki/Nasa/'
# # # # # #1-my_str[10:19],Returns the characters in indices 10-18.
# # # # # print(f'1-',my_str[10:19])
# # # # # #2-my_str[10:-5],Returns the characters in indices 10-28.
# # # # # print(f'2-',my_str[10:-5])
# # # # # #3-my_str[8:],Returns all characters from index 8 until the end of the string.
# # # # # print(f'3-',my_str[8:])
# # # # # #4-my_str[:23],Returns every character up to index 23, but not including my_str[23].
# # # # # print(f'4-',my_str[:23])
# # # # # #5-my_str[:-1],Returns all but the last character.
# # # # # print(f'5-',my_str[:-1])
# # # # # #6-stride argument my_str[::]
# # # # # print(f'6-',my_str[::])
# # # # # #7-stride argument my_str[::2] print every other character
# # # # # print(f'7-',my_str[::2])
# # # # # #8-stride argument my_str[1:9:3] print every third character
# # # # # print(f'8-',my_str[1:9:3])

# # # # # start_index = int(input())
# # # # # end_index = int(input())
# # # # # my_string = 'Jack be nimble, Jack be quick'

# # # # # ''' Your code goes here '''
# # # # # my_str=my_string[start_index:end_index]
# # # # # sliced_lyric=my_str

# # # # # print('Full lyric:', my_string)
# # # # # print('Sliced lyric:', sliced_lyric)


# # # # full_saying = input()

# # # # p_saying=full_saying[1:-1]
# # # # partial_saying=p_saying

# # # # print(partial_saying)

# # # my_string = input()
# # # sub_string=my_string[:3] + my_string[-2:]
# # # print(sub_string)

# # full_string = input()

# # ''' Your code goes here '''
# # sub_lyric=full_string[len(full_string)//2:][::3]

# # print(sub_lyric)

# print(f'{"Player Name":16}{"Goals":8}{"score":6}')

# print('-' * 50)


# print(f'{"Sadio Mane":16}{"22":8}{5:6}')

# print(f'{"Gabriel Jesus":16}{"7":8}{6:6}')
# print()

print(f'{5:4.1f}')