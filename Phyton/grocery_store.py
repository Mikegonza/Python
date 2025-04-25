# Grocery prices
purchase = {
    "bananas": 1.85,
    "steak": 19.99,
    "cookies": 4.52,
    "celery": 2.81,
    "milk": 4.34
}

# Read item and quantity
item = input()
quantity = int(input())

# Base total
price = purchase[item]
total = price * quantity

# Apply discount
if 10 <= quantity <= 20:
    total *= 0.95
elif quantity >= 21:
    total *= 0.90

# Output result
print(f"{item} ${total:.2f}")
