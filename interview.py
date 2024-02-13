newString = 'My Name isssssss Abdul'

# longest=newString[-5:]
# print(longest)

words = newString.split()
longest_word=max(words, key=len)
print(longest_word)

#######################################

# number='Today is 30th January 2024'

# for i in number:
#     if i.isdigit():
#         print(i, end='')