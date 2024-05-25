'''a = 4           #int
b = 3.14        #float
c = 'salom'     #str (string)
d = True        #bool (boolean)
print('a =',a, type(a))
print('b =',b, type(b))
print('c =',c, type(c))
print('d =',d, type(d))
x = a + b + c
print(x)'''

'''a = int(input('a ='))
b = int(input('b ='))
x = a + b
y = x / 2
print('x =',x)
print('y =',y)'''

'''ism = input('ismingiz ->')
fam = input('familiyangiz ->')
print('assalomu aleykum ',fam,ism)'''



'''a = int(input('a ='))
b = int(input('b ='))
if a > b:
    print('a katta')
else:
    if a == b:
        print('a teng b ga')
    else:
        print('b katta')'''

'''
m_parol = 'salom2'
k_parol = input('parolingiz ->')
if k_parol == m_parol:
    print("parol to'g'ri")
else:
    print("parol noto'g'ri")'''

'''
i = 1
while i < 6:
    print(i)
    i = i + 1'''
'''
i = 6
while i > 0:
    print("salom dunyo 1")
    print("salom dunyo 2")
    print("salom dunyo 3")
    print("salom dunyo 4")
    #i = i - 1

'''



'''
while True:
    print('salom')
    son = int(input("sonni kiriting --> "))
    for x in range(1,10 + 1,1):
        p = son * x
        print(son, '*',x,'=',p)
    print('men',son,"karrani chiqardim")'''




'''

import time
sanoq = 0
while True:
    s_pass = 'salom'
    k_pass = input('parolni kiriting -->')    
    if s_pass == k_pass:
        print("parol to'g'ri  !!!!!")
        sanoq = 0
    else:
        print("parol noto'g'ri")
        sanoq += 1        
        print('siz ',sanoq,'martta xato terdiz')
        if sanoq == 5:
            for i in range(1,5+1):
                print(i,'- soniya')
                time.sleep(1)            
        if sanoq == 7:
            for i in range(1,7+1):
                print(i,'- soniya')
                time.sleep(1)            
        if sanoq == 9:
            print('xayir    ')
            break
       
'''

import time
while True:
    for i in range(3):
        print('sariq')
        time.sleep(1)
    print('qizil !!!!!')
    time.sleep(5)
    for i in range(3):
        print('sariq')
        time.sleep(1)
    print('yashil  --->')
    time.sleep(5)   
    t = time.localtime()
    hammasi = time.strftime("%H:%M:%S", t)
    minut = time.strftime("%M", t)  #"%H:%M:%S"
    print(hammasi)
    print(minut)
    print(type(int(minut)))
    if int(minut) == 15:
        print('sariq   maktab vaqti')
        time.sleep(40)  #minit 15 ga teng bo'lganda 40 sekunt kutadi























