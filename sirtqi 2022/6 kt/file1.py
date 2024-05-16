'''f = open("qwer.txt", "r")
print(f.read())'''

f = open("qwer.txt", "w")
f.write("salom ")
f.close()

f = open("qwer.txt", "r")
print(f.read())
