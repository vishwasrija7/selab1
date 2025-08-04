# Read a sentence from the user
sentence = input("Enter a sentence: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize a counter
vowel_count = 0

# Loop through each character in the sentence
for char in sentence:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels
print("Number of vowels:", vowel_count)
 