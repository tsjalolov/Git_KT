'''f = open("myfile.txt", "r")
print(f.read())'''
L = ["Bu Delhi \n", "Bu Paris \n", "Bukhara \n"]
 
# Creating a file
with open("myfile1.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    
    file1.close()  # to change file access modes
 
with open("myfile1.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())

