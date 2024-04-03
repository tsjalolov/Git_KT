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
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
c1 = x+y+z/2
c2 = x*y*z

if c1 < c2:
    print('+ kichik', c1**2 +1)
elif c2 < c1:
    print('* kichik', c2**2 +1)
else:
    print('=', c1**2 +1)



# 6.4
'''x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x > y and y > z:
    print('True')
else:
    print('False')'''
