'''a = int(input('a= '))
b = float(input('b= '))
c = input('c =')         #str
d = a + b
print('a = ',a, type(a))
print('b = ',b, type(b))
print('c = ',c, type(c))
print('d = ',d, type(d))
if a < 9:
    print('a sonimiz 9 dan kichik')
else:
    print('a sonimiz 9 dan katta')'''
'''men = int(input('mening yoshim = '))
sen = int(input("do'stimning yoshi= "))

if men > sen:
    yosh  = men - sen
    print('men sendan ',yosh,'yosh katta')
else:
    yosh = sen - men
    print('men sendan ',yosh,'yosh kichik')'''










'''a = int(input('a= '))
b = int(input('b= '))
if a > b:
    print('a son katta ')
else:
    if a == b:
        print('a = b')
    else:
        print('b son katta ')'''


'''x = int(input('x= '))
if x >= 1 and x <= 10:
    print('xato')
else:
    print("to'g'ri")'''

'''#juft sonlar
i = 2
while i <= 30:
    print('salom ->>',i)
    i = i + 2'''
'''x = int(input('x= '))
i = 1
while i <=x:
    print(i)
    i = i + 1'''

'''n = int(input('n son = '))
s = 0
i = 1
while i <=n:
    print(i)
    s = s + i
    i = i + 1
print('s=',s)'''

'''while True:
    n = int(input('n son = '))
    i = 0
    while i <10:
        i = i + 1
        p = i * n
        if i == 5 or i == 8:
            print('<<--------->>')
            continue
        print(n,'*',i,'=',p)'''


'''i = 1
while i <= 5:
    print(i)
    i = i + 1

for x in range(1,5+1,1):
    print(x)'''
'''
s = 'salom sizga'
for x in s:
    print(x)
    if x == 'm':
        break
    
print('<<<--->>>')


i = 0
while i < len(s):
    print(s[i])
    i = i + 1'''


'''import time
s = 0
for i in range(1,2,1):
    print('<--soat ',i,'-->')
    for j in range(1,10+1,1):
        print('<---minut ',j,'--->')
        for k in range(1,60+1,1):
            s = s + 1
            time.sleep(1)
            print('<------sekund ',k,'------>')
print(s, 'sekund bor')'''
import time
from datetime import datetime
now = datetime.now()
print(now)
while True:
    print('qizil XXXXX')
    time.sleep(5)
    print('sariq ----')
    time.sleep(2)
    print('yashil >>>>')
    time.sleep(5)
    print('sariq ----')
    time.sleep(2)









    



