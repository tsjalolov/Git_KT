'''a = int(input('a='))
b = float(input('b='))
d = input("so'zni kiriting->>")
c = a + b
x = d + str(a) + str(b)
print('c=',c)
print('a=',a, type(a))
print('b=',b, type(b))
print('d=',d, type(d))
print('x=',x, type(x))'''

'''a = int(input('a='))
b = int(input('b='))
if a > b:
    print('a katta')
else:
    if a == b:
        print('a = b')
    else:
        print('b katta')'''








'''a = int(input('a='))
i = 1
S = 0
while i <= a:
    S = S + i
    print('salom',i)
    i = i + 2
print('S = ',S)'''

'''from math import *
a = sqrt(4) * pow(3,2)
print(a)'''

'''
x = 'ha'
while x == 'ha':
    n = int(input('n='))
    i = 0
    while i < 10:        
        i = i + 1
        p = n * i
        if i == 5 or i == 8:
            print('<<----->>')
            continue
        print(n, '*',i, '=',p)
    x = input("davom ettirasizmi? ha/yo'q ")
print('dasturimiz tugadi xayr....')
'''
'''
s = 0
J_summa = 0
i = 1
while i <= 5:
    print('<<--1-->>')
    i = i + 1    
    j = 1
    while j <= 4:
        print('<<-2->>')
        j = j + 1
        k = 1
        J_summa = J_summa + 1
        while k <= 4:
            print('<-3->')
            k = k + 1
            s = s + 1
print("while to'liq ",s,"martta aylandi.", 'j esa ',J_summa,"martta aylandi.")
'''
'''i = 1
while i <= 4:
    print('salom')
    i= i + 1

print('----------')

for x in range(1,50+1,1):
    print('salom', x)'''

'''
for i in range(1,10+1,1):
    natija = 5 * i
    print(5,'*',i,'=',natija)'''


import time
from datetime import datetime

now = datetime.now()
print(now)
while True:
    print('qizil XXXXXXX')
    time.sleep(5)
    print('sariq ---')
    time.sleep(2)
    print('yashil --->>>>>>>>')
    time.sleep(5)
    print('sariq ---')
    time.sleep(2)
    
    








