i=int(input("Enter number to check Amstrong:"))
orig=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10

if orig == sum:
    print("Amstrong")

else:
    print("Not Amstrong")