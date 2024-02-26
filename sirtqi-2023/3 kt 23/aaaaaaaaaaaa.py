f = open("d1emofile.txt", "r")
print(f.read())



L = ["Bu Delhi \n", "Bu Paris \n", "Bu London \n"]
print(L) 
# Creating a file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    print('-----------')
    
    file1.close()  # to change file access modes

 
with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())

