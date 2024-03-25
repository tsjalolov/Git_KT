'''# 6.5
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a >= b and b >= c:
    a = a*2
    b = b*2
    c = c*2
else:
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if c < 0:
        c = c * -1
print('a=',a,'b=',b,'c=',c)'''
'''login = 'fedya'
password = 'qwert12345'
x1 = input('loginni kiriting --> ')
x2 = input('parolni kiriting --> ')
if x1 == login and x2 == password:
    print('uraa')
else:
    print('kechirasiz')'''
'''# 6.6
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    z = x - y
else:
    z = y - x + 1
print('z=',z)'''
#6-7
'''a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print('a =',a)
else:
    print('a =',a,'b =',b)'''

a = int(input('a = '))
b = int(input('b = '))
if a <= b:
    a = 0
print('a =',a)
    
