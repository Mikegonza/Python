# Define the fixed distances per employee
distances = {
    'A': 15.62,
    'B': 41.85,
    'C': 32.67
}

# Read inputs
trips_A = int(input())
trips_B = int(input())
trips_C = int(input())

# Calculate total distance
total_distance = (trips_A * distances['A'] +
                  trips_B * distances['B'] +
                  trips_C * distances['C'])

# Output in required format
print(f"Distance: {total_distance:.2f} miles")
