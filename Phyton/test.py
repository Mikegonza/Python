species_1 = "Sandhill Crane"
count_1 = 550
region_1 = "Midwest"
species_2 = "Blackpoll Warbler"
count_2 = 700
region_2 = "Southwest"

THRESHOLD = 500

#The use of the and operator does ensure that both conditions must be true for the result to be true, which is crucial for our logic.
species_1_high = region_1 != "Midwest" and count_1 > THRESHOLD# YOUR CODE HERE
species_2_high = region_2 != "Midwest" and count_2 > THRESHOLD# YOUR CODE HERE
print(f"Unusual pattern for {species_1}: {species_1_high}")
print(f"Unusual pattern for {species_2}: {species_2_high}")

# Expected output:
# Unusual pattern for Sandhill Crane: False
# Unusual pattern for Blackpoll Warbler: True