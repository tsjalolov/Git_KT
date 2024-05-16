#6-1-1
'''x = int(input('x='))
y = int(input('y='))
if x > y:
    print('x katta')
else:
    if y > x:
        print('y katta')
    else:
        print('x va y teng')'''

#6-1-2
'''x = int(input('x='))
y = int(input('y='))
if x < y:
    print('x kichik')
else:
    if y < x:
        print('y kichik')
    else:
        print('x va y teng')'''

#6-2
'''x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
print('kattasi -->',max(x,y,z))
if x > y and x > z:
    print('x katta')
else:
    if y > x and y > z:
        print('y katta')
    else:
        if z > x and z > y:
            print('z katta')
        else:
            print('tenglik bor')'''
#6.4  
'''
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x > y and y > z:
    print('qanoatlantiradi')
else:
    print('qanoatlantirmaydi')'''
#6.5
'''a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
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
print('a = ',a, 'b = ', b, 'c = ', c)'''

#6.6
'''x = int(input('x='))
y = int(input('y='))

if x > y:
    z = x - y
else:
    z = y - x + 1
print('z=',z)'''

#6.7 
'''a = int(input('a='))
b = int(input('b='))
if a > b:
    print('a=',a)
else:
    print('a=',a,'b=',b)'''

#6.8
'''a = int(input('a='))
b = int(input('b='))
if a <= b:
    a = 0
print('a=',a,'b=',b)'''
#6.9
'''a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a > 1 and a < 5:
    print('a kiradi')
else:
    print('a not')
if b > 1 and b < 5:
    print('b kiradi')
else:
    print('b not')
if c > 1 and c < 5:
    print('c kiradi')
else:
    print('c not')'''
#6.10
'''a = float(input('a='))
b = float(input('b='))
if a < b:
    a1 = (a + b)/2
    b =  a * b * 2
    a = a1
else:
    b1 = (a + b)/2
    a =  a * b * 2
    b = b1
print(a,b)'''
#6.11
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a > 0:
    print('a2 =', a**2)
if b > 0:
    print('b2 =', b**2)
if c > 0:
    print('c2 =', c**2)


