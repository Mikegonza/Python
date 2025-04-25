# Read filename from input
filename = input()

# Step 1: Read the first 3 words
with open(filename, "r") as f:
    words = [line.strip() for line in f.readlines()[:3]]

# Step 2: Form the sentence
sentence = " ".join(words)

# Step 3: Append the sentence to the file
with open(filename, "a") as f:
    f.write(sentence + "\n")

# Step 4: Read and print full file content
with open(filename, "r") as f:
    print(f.read())
