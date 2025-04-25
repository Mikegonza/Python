# Stocks dictionary
stocks = {
    'TSLA': 912.86,
    'BBBY': 24.84,
    'AAPL': 174.26,
    'SOFI': 6.92,
    'KIRK': 8.72,
    'AURA': 22.12,
    'AMZN': 141.28,
    'EMBK': 12.29,
    'LVLU': 2.33
}

# Read number of stock selections
n = int(input())

# Read n stock symbols
total = 0
for _ in range(n):
    symbol = input()
    total += stocks[symbol]

# Print total cost formatted
print(f"Total price: ${total:.2f}")
