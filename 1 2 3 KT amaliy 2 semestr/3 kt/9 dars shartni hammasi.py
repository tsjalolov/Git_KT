


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
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x > y and y > z:
    print('qanoatlantiradi')
else:
    print('qanoatlantirmaydi')'''
# 6.5
'''a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a >= b and b >= c:
    a = a * 2
    b = b * 2
    c = c * 2    
else:
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if c < 0:
        c = c * -1
print('a=',a,'b=',b,'c=',c)'''

#6.6
'''x = int(input('x = '))
y = int(input('y = '))
if x > y:
    z = x - y
else:
    z = y - x + 1
print(x,y)'''

#6.7
'''x = int(input('x = '))
y = int(input('y = '))
if x > y:
    print(x)
else:
    print(x,y)
'''
#6.8
'''x = int(input('x = '))
y = int(input('y = '))
if x >= y:
    x = 0
print(x,y)'''

#6.9
'''a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > 1 and a < 5:
    print('a kiradi')
if b > 1 and b < 5:
    print('b kiradi')
if c > 1 and c < 5:
    print('c kiradi')'''

#6.10
'''a = int(input('a = '))
b = int(input('b = '))

if a < y:
    a1 = (a + b)/2
    b = a * b * 2
    a = a1
else:
    b1 = (a + b)/2
    a = a * b * 2
    b = b1
print(x,y)'''

#6.13 kvadrat tenglama

from math import sqrt
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a == 0:
    print('chziqli tenglama')
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print("bo'sh to'plam")
    else:
        if D == 0:
            x1 = -b/(2 * a)
            print('x1=',x1)
        else:
            x1 = (-b + sqrt(D))/(2 * a)
            x2 = (-b - sqrt(D))/(2 * a)
            print('x1=',x1,'x2=',x2)
            





