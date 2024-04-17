# i= int(input("Enter to number to check palindrome:"))

# rev=0
# x=i
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10

# if(x==rev):
#     print("Number is Palindrome")
# else:
#     print("number is not plaindrome")

i = 333

rev = 0
x=i

while i>0:
    rev = (rev*10)+i%10
    i=i//10

if (x==rev):
    print("Number is Palindrome")

else:
    print("Number is not Palindrome")
    