'''a = 5           #int
b = 4.8         #float
c = 'salom'     #str (string)
t = True        #bool (bulean)
print('a = ', a, type(a))
print('b = ', b, type(b))
print('c = ', c, type(c))
print('t = ', t, type(t))'''





'''a = int(input('a ='))
b = int(input('b ='))
x = a + b
y = x/2
print('x=',x)
print('y=',y)'''

'''ism = input('ismingizni kiriting ')
fam = input('familiyangizni kiriting')
print('assalomu aleykum ', fam, ism)
'''


'''a = int(input('a ='))
b = int(input('b ='))
if a > b:
    print('a soni katta')
else:
    if a == b:
        print('a = b ga')
    else:
        print('b soni katta')
print(a,b)'''


'''
import hashlib
h2 = hashlib.new('sha256')
h = hashlib.new('sha256')
h.update(b"salom2")
#print(h.hexdigest())
a = input('parolni kiriting  ')
h.update(b'')
if parol == a:
    print("parol to'g'ri")
else:
    print('parol xato kiritildi')'''

# for va while
'''for i in range(2,51,2):
    if i == 4:
        print('>>>>>>>>>><<<<<<<<<')
        continue
    print('salom -->',i)'''


'''son = int(input('sonni kiriting -> '))
for i in range(1,11,1):
    natija = son * i
    print(son, '*',i,'=',natija)'''


'''   
for i in range(4):
    m_parol = 'pass_salom'
    k_parol = input('pass --> ')
    if m_parol == k_parol:
        print('uraaa')
        break
    else:
        print('parol xato')
else:
    print('4 martta urindingiz uzur')'''



import time
sanoq = 0
while True:
    m_pass = 'salom'
    k_pass = input('parolni kiriting -->')
    #print('bizning parol    -->',m_pass)
    #print('kiritilgan parol -->',k_pass)
    if m_pass == k_pass:
        print(">>>> to'g'ri <<<<")
        sanoq = 0
    else:
        print("---- xato -----")
        sanoq +=1
        print('siz ',sanoq,'- martta xato terdingiz')
        #time.sleep(5)
        if sanoq == 5:
            print('5 sekund kuting')
            for i in range(1,5+1):
                print(i, '- soniya')
                time.sleep(1)           
        if sanoq == 7:
            print('7 sekund kuting')
            for i in range(1,7+1):
                print(i, '- soniya')
                time.sleep(1)
        if sanoq == 9:
            print('xayir   !!!!')
            break
            
            




'''
import time
while True:
    for i in range(1,4):
        print('sariq')
        time.sleep(1)
    print('qizil   !!!!!')
    time.sleep(5)
    for i in range(1,4):
        print('sariq')
        time.sleep(1)
    print('yashil ---->>>>>>>')
    time.sleep(5)
'''








