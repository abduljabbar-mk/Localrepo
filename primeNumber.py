# n=int(input("Enter number:"))

# count=0
# i=1
# while i<=n:
#     if(n%i==0):
#         count = count+1
#     i=i+1
    
# if(count==2):
#     print("its Prime Number")
# else:
#     print("Not Prime")

num = 13

count = 0
i =1

while i <=num:
    if (num%i==2):
        count = count +1
    i= i+1
    
if(count ==2):
    print('prime')
else:
    print('Not prime')