# Read temperature input
temp = int(input())

# Determine water state
if temp < 33:
    state = "Frozen"
elif temp <= 80:
    state = "Cold"
elif temp <= 115:
    state = "Warm"
elif temp <= 211:
    state = "Hot"
else:
    state = "Boiling"

# Optional safety comment
safety_comment = ""
if temp == 212:
    safety_comment = "Caution: Hot!"
elif temp < 33:
    safety_comment = "Watch out for ice!"

# Print output
print(state)
if safety_comment:
    print(safety_comment)
