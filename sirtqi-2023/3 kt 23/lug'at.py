talaba1 = {
    "ism": "Sharifa",
    "familiya": "Isomova",
    "year": 2004
}
talaba2 = {
  "ism": "Javohir",
  "familiya": "Muhammedov",
  "year": 2004
}
talaba3 = {
  "ism": "Zarina",
  "familiya": "Muhiddinova",
  "year": 2005
}
#print(talaba1)
#print(talaba2)
#print(talaba3)

#           0       1       2
mass = [talaba1,talaba2,talaba3]
print(mass)
print('------------')
for i in mass:
    #print(i)
    
    for j in i:
        if j == 'year':
            print(i[j])





'''
for j in mass:    
    for i in j:
        print(j[i])'''
      
