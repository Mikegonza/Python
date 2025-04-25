result = 0

for n in range(6):
    result = n - 4
    
    if (result % 2) != 0:
        print('_', end=' ')
        continue
    
    print(result, end=' ')

print('done')

print('\n')
a = int(input())
b = int(input())
c = int(input())

while a < b:
    print(a)
    
    if a > c:
        break
    
    a += 2

print('\n')

stop = int(input())

for a in range(5):
    result = 0
    
    for b in range(3):
        result += a + b
    
    print(result)
    
    if result > stop:
        break
print('\n')

stop = int(input())
result = 0

for a in range(4):
    print(a + 1, end=': ')
    
    for b in range(3):
        result += a + 1
        
        if result > stop:
            print('_', end=' ')
            continue
        
        print(result, end=' ')
    
    print()