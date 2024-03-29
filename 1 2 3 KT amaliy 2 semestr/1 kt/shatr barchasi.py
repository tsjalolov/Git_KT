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


x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
print('kattasi -->',max(x,y,z))
if x > y and x > z:
    print('x katta')
else:
    if y > x and y > z:
        print('y katta')
    else:
        if z > x and z > y:
            print('z katta',z)
        else:
            print('tenglik bor')
