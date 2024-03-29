# 6.9
'''a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > 1 and a < 5:
    print(' a soni kiradi')
if b > 1 and b < 5:
    print(' b soni kiradi')
if c > 1 and c < 5:
    print(' c soni kiradi')
print('a=',a,'b=',b,'c=',c)'''
# 6.10
'''x = int(input('x = '))
y = int(input('y = '))

if x < y:
    x1 = (x + y)/2    
    y = x * y * 2
    x = x1
else:
    y1 = (x + y)/2
    x = x * y * 2
    y = y1
print('x=',x,'y=',y)'''
# 6.12
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('c = '))

if d >= c and c >= b and b >= a:
    a,b,c = d
else:
    if not(a>b and b>c and c>d):
        a = a**2
        b = b**2
        c = c**2
        d = d**2
print(a,b,c,d)
