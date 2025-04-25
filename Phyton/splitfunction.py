bird_tag = "Hummingbird-456"
distance_string = "distance:575"
bird_name = bird_tag.split("-")[0]  # Extract bird name
bird_id = int(bird_tag.split("-")[1])  # Extract bird ID
distance_traveled= int(distance_string.split(":")[1]) #Extract Distance Traveled
distance_traveled>500

print("Bird Name:", bird_name)
# TODO: print the bird_id
print("Bird id:", bird_id)
# TODO: print the distance traveled
print("Distance Traveled:", distance_traveled, "miles")
# TODO: print the condition over 500
print("Over 500 miles?", distance_traveled>500)

# Expected output
# Bird Name: Hummingbird
# Bird ID: 456
# Distance Traveled: 575 miles
# Over 500 miles? True