str = 'My Name is Abdul'
# Splitting the string into words
words = str.split()

# Finding the longest word
longest_word = max(words, key=len)

print(f"The longest word is: {longest_word}")