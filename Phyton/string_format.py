# List of frameworks
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# Read integer input
try:
    index = int(input())
    print(frameworks[index])
except:
    print("Error")
