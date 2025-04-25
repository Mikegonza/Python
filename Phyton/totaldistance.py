name_1 = "Sandhill Crane"
distance_1 = 250
time_1 = 12
name_2 = "Blackpoll Warbler"
distance_2 = 360
time_2 = 8
crane_speed = distance_1 / time_1
warbler_speed = distance_2 / time_2

# Compare speeds
total_distance_per_day = (crane_speed + warbler_speed) * 24

# Print results
print(name_1, "Speed:", crane_speed, "miles per hour")
print(name_2, "Speed:", warbler_speed, "miles per hour")
#you can convert a number to a string by using the str() function.
print("Total distance per day: " + str(total_distance_per_day))