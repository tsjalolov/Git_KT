''' A = int(input('A = '))
a = int(input('a = '))
b = int(input('b = '))
c = a + b + A
print('a + b + A = ',c) 

a = int(input('olmaning KG = '))
b = int(input('anorning KG = '))

if a > b:
    c = a - b
    print('olma anordan ',c , "KG ko'p")
else:
    if a == b:
        print('anor olmaning KG siga teng ')
    else:
        c = b - a
        print('anor olmadan ',c , "KG ko'p")
'''
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
d = 0
if a == 5:
    d = 1
    print('A soni =',a)
if b == 5:
    d = 1
    print('B soni =',b)
if c == 5:
    d = 1
    print('C soni =',c)

if d == 0:
    print('A , B , C sonlar orasida 5 raqami yo`q')   
