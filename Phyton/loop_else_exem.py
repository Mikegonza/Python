result = 1
n = 3
while n < 8:
    print(n, end=' ')
    result *= 4
    n += 1
else:
    print(f'\ {result}')
print('done')

print('\n')

result = 0
n = 2
while n < 8:
    print(n, end=' ')
    result += 3
    if result > 10:
        print('!')
        break
    n += 1
else:
    print(f'/ {result}')
print('done')

print('\n')

result = 1
for n in range(3):
    print(n, end=' ')
    result *= 3
else:
    print(f'| {result}')
print('done')

print('\n')

stop = -13
total = 0
for number in [5, 6, 7, 4, 7, 2]:
    print(number, end=' ')
    total -= number
    if total <= stop:
        print('$')
        break
else:
    print(f'\ {total}')
print('done')