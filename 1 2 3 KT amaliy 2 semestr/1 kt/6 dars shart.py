'''#6.3.1
# max(a+b+c, a*b*c)
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
c1 = a+b+c
c2 = a*b*c
if c1 > c2:
    print('+ katta ',c1)
else:
    if c2 > c1:
        print('* katta ',c2)
    else:
        print(' = ',c2)'''
#6.3.2   c1       c2
# min2(a+b+c/2, a*b*c) + 1
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
c1 = a+b+c/2
c2 = a*b*c
if c1 < c2:
    c1 = c1 ** 2 + 1
    print('+ kichik ',c1)
else:
    if c2 < c1:        
        c2 = c2 ** 2 + 1
        print('* kichik ',c2)  
    else:
        print(' = ',c2)
