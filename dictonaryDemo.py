# mydic = {101:'x', 102:'y', 103:'z'}
# # print(mydic)

# # print(mydic[101])
#reading itams for dictonary
mydic ={
    "Brand":"Hyundai",
    "Model": "i10",
    "year": "2021"
}

# print(mydic["Brand"])

# mydic["year"]='2022'
# print(mydic)

# for i in mydic:
#     # print(i) # for printing only keys
#     print(mydic(i))


# for i in mydic.values():        #Only values
#     print(i)
    
# for x,y in mydic.items():        # Both key and value
#     print(x, y)
    
# for i in mydic.keys():          # print only Keys
#     print(i)

#ex.5:- check key is exist in dictonary or not
# if "Model" in mydic:
#     print("Exist")
# else:
#     print("Not exists")

#Ex.6 adding iems to dict
# mydic["Colour"]="Red"
# print(mydic)

#Remove items for dict
# mydic.pop("year")
# print(mydic)

# mydic.clear()
print(mydic)

#copying dict
# mydic2=mydic
# print(mydic2)

#copying using copy() function

mydic2=mydic.copy()
print(mydic2)