colors = ['blue', 'red', 'black', 'yellow']
for (position, color) in enumerate(colors):
    print(position, color)


numbers = [-4, 9, 4, 5]
for (position, number) in enumerate(numbers):
    if number < 0:
        print(position, 'x')
    else:
        print(position, number)


