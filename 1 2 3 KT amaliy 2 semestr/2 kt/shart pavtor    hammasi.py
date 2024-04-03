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

x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x > y and y > z:
    print('qanoatlantiradi')
else:
    print('qanoatlantirmaydi')
