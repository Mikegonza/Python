weights = [3, 5, 4, 8]
result = 0
for weight in weights:
    result -= weight
print(result)


cities = {
    'Chicago': 309,
    'Austin': 5259,
    'London': 550,
    'Nairobi': 3435,
    'Montreal': 958,
    'Toronto': 584,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)