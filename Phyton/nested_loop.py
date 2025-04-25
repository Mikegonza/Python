c1 = 'a'
while c1 < 'b':
    c2 = 'a'
    while c2 <= 'c':
        print(f'{c1}{c2}', end = ' ')
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)

print('\n')

i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}', end=' ')
        i2 = i2 + 3
    i1 = i1 + 10

print('\n')

count = 0
for i in range(5):
    for j in range(3):
        count = count + 1
print(count)

print('\n')

letter1 = 'j'
while letter1 < 'l':
    letter2 = 't'
    while letter2 <= 'v':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

print('\n')

i = 3
while i < 20:
    j = 5
    while j <= 11:
        print(f'{i}{j}')
        j = j + 4
    i = i + 14

print('\n')

num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    for j in range(num_cols):
        print('*', end=' ')
    print()

print('\n')

num_rows = int(input())
num_cols = int(input())

row = 1

while row <= num_rows:
    col=0  
    while col < num_cols:  
        letter = chr(ord('A') + col)
        print(f'{row}{letter}', end=' ')
        col += 1
    row += 1
print()

print('\n')
