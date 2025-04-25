#Many user-created passwords are simple and easy to guess. Write a program that takes a simple password 
#and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.
#i becomes 1
#a becomes @
#m becomes M
#B becomes 8
#s becomes $
#Ex: If the input is: mypassword
#the output is: Myp@$$word!

# Define the replacement mapping
replacements = {
    'i': '1',
    'a': '@',
    'm': 'M',
    'B': '8',
    's': '$'
}

# Get user input
word = input()

# Build the new password
password = ''
for char in word:
    if char in replacements:
        password += replacements[char]
    else:
        password += char

# Append '!' at the end
password += '!'

# Output the stronger password
print(password)
