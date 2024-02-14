newString = 'My Name is Abdul'

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

##########################################

str = "Banagalore is my city and i am living here peasfully."

for i in str:
    if i == 'a':
        continue
    print(i, end="")

# # s = str.replace('a', '')
# # print(s)

# # s = str[::-1]
# # print(s)


# s = 'My name is abdul abd todays date is 30th november 2021'

# for i in s:
#     if i.isdigit():
#         print(i, end='')

s = 'My name is abdul abd todays date is 30th november 2021'

for i in s:
    if i.isdigit():
        print(i, end='')