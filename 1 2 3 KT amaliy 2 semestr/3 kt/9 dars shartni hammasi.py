


#6.3.1
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
c1  = x + y + z
c2  = x * y * z
#print(max(c1,c2))
if c1 > c2:
    print('+ katta',c1)
else:
    if c2 > c1:
        print('* katta',c2)
    else:
        print('= teng',c2)'''
#6.3.2
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
c1 = x+y+z/2
c2 = x*y*z
if c1 < c2:
    print('+ kichik',c1**2 + 1)
elif c2 < c1:
    print('* kichik',c2**2 + 1)
else:
    print('+ == *',c2**2 + 1)'''
#6.4
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x > y and y > z:
    print('qanoatlantiradi')
else:
    print('qanoatlantirmaydi')


