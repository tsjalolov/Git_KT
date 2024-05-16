#6.1
'''x = int(input('x = '))
y = int(input('y = '))
print('kattasi -->',max(x,y))
if x > y:
    print('x katta')
else:
    if y > x:
        print('y katta')
    else:
        print('x = y')'''

#6.2
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
print('kattasi -->',max(x,y,z))
if x > y and x > z:
    print('x katta',x)
else:
    if y > x and y > z:
        print('y katta',y)
    else:
        if z > x and z > y:
            print('z katta',z)
        else:
            print('tenglik bor')'''
#6.3.1
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
c1 = x+y+z
c2 = x*y*z
if c1 > c2:
    print(' + katta')
elif c2 > c1:
    print('* katta')
else:
    print('= teng')'''

#6.3.2
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
c1 = x+y+z/2
c2 = x*y*z

if c1 < c2:
    print('+ kichik', c1**2 +1)
elif c2 < c1:
    print('* kichik', c2**2 +1)
else:
    print('=', c1**2 +1)'''



# 6.4
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x > y and y > z:
    print('True')
else:
    print('False')'''
#6.5
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
print('z=',z)'''

#6.13 kvadrat tenglama
'''from math import sqrt
a = float(input('a = '))
b = float(input('b = ')) 
c = float(input('c = '))
if a == 0:
    print('bu chiziqli tenglama')
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print(' yechimga ega emas!!!')
    else:
        if D == 0:
            x1 = -b/ (2 * a)
            print('x1 = ',x1)
        else:
            x1 = (-b + sqrt(D))/(2 * a)
            x2 = (-b - sqrt(D))/(2 * a)
            print('x1 = ',x1,'x2 = ',x2)'''



        

