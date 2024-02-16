# Writing data into text file
# file = open("C:/Users/Asus/OneDrive/Desktop/DA_Docs/Testing_Doc.txt", "w")
# file.write("This is a first Line....\n")
# file.write("This is a Second Line....\n")
# file.write("This is a Third Line....\n")
# file.write("This is a Fourth Line....\n")
# file.write("This is a fifthLine....\n")
# file.write("This is a Sixth Line....\n")
# file.write("This is a Seventh Line....")

# file.close()
# print("Excecuted successfull")

###################################################

# Read the File
# file = open("C:/Users/Asus/OneDrive/Desktop/DA_Docs/Testing_Doc.txt", "r")
# print(file.read())
# file.close

#######################################################
#Appending data in to file
file = open("C:/Users/Asus/OneDrive/Desktop/DA_Docs/Testing_Doc.txt", "a")
file.write("\nThis is a Eigth Line....\n")
file.write("This is a ninth Line....")
file.close()
print("Executed Successfully")
