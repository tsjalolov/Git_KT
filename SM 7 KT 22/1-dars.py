'''print('salom')
a = 9 # int
b = 3.5  # float
s  = "salom" #str
#c = a + b
#d = c/2
print(a,'-->',type(a))
print(b,'-->',type(b))
print(s,'-->',type(s))# odiljon faqat siz eshitmayapsiz
'''
'''a = int(input('a sonni kiriting -->'))
b = int(input('b sonni kiriting -->'))
print('a=',a)
print('b=',b)
'''

'''
while True:
    ism = input('ismingizni kiriting -->')
    familiya = input('familiyangizni kiriting -->')
    yil = int(input('yilingizni kiriting -->'))
    yil2 = int(input("o'rtog'imning yili -->"))
    yosh = 2024 - yil
    print('assalomu aleykum',familiya,ism,'siz',yosh,'yoshdasiz')
    farq = yil - yil2 
    #       2000 - 2009  = -9   <  0 
    if farq < 0:
        x = farq * -1   # x = -9 * -1   =9
        print("men o'rtog'imdan ",x,'yosh katta man')
    else:           #2009 - 2000  = 9   <  0
        if yil == yil2:
            print("biz o'rtog'im bilan tengdoshmiz")
        else:
            print("men o'rtog'imdan ",farq,'yosh kichik man')


'''





'''



a = int(input('a sonni kiriting -->'))
b = int(input('b sonni kiriting -->'))
if a > b:
    print('a soni katta a=',a)
    print('b soni kichik b=',b)
else:
    if a == b:
        print('a soni teng b soniga')
    else:
        print('b soni katta b=',b)
        print('a soni kichik a=',a)

'''



'''
n = 1
while n <= 5 : # True  False
    print('salom ',n)
    n = n + 1    
print('dastur tugadi !!!')
'''


'''
for i in range(1,5+1,1): #(0,5,1)
    if i == 3:
        print('men 3 raqamini chiqarmayman')
        continue
    print(i) 
print('for operatorli dastur tugadi !!!')



for i in range(1,5+1,1): #(0,5,1)
    if i == 3:
        print('men 3 keyin chiqarmayman')
        break
    print(i) 
print('for operatorli dastur tugadi !!!')
 '''

'''s = 0
for i in range(1,100+1,1): #(0,5,1)
    s = s + i
print(s)'''




'''
x = "salom sizga "

for i in x:
    if i == 'a':
        continue
    print(i)'''




''' 
x = input("so'zni kiriting a harfini sanaymiz --> ")
S = 0
for i in x:
    if i == 'a':
      S = S + 1  
print(x, "--> so'zida ",S,' ta a harfi qatnashgan')
'''


'''
while True:
    n = int(input('sonni kiriting-->'))
    for i in range(1,11,1):
        k = n * i
        print(n, '*', i,'=',k)
'''







#kartej yoki massivlar
'''
#         0 1    2      3    4
massiv = [1,4,'salom','biz',True]
print(massiv)
print('massivimizning uzunligi -->',len(massiv))
for i in massiv:
    print(i)'''


'''#         0 1    2      3    4
massiv = [1,4,'salom','biz',True]
i = 0 
while i < len(massiv):  # len(massiv) = 5
    print(massiv[i])
    i = i + 1'''

'''#    01234567
m = 'salom sizga'
print(m[:5])
for i in m:
    print(i)'''



'''
kun = int(input('hafta kunini kiriting-->'))
#         0     1    2      3    4      5     6
hafta = ('du','se','chor','pay','juma','sha','ya')
print(hafta[kun - 1])
'''

# lug'at 
'''
lugat_1 = {
    'marka':"chevrolet",
    'model':'cobalt',
    'yil':'2024'}
lugat_2 = {
    'marka':'chevrolet',
    'model':'Malibu',
    'yil':'2023'}
mass = [lugat_1,lugat_2]


for i in mass:
    print(i['model'],'-->',i['yil'])'''

'''

while True:
    hafta = {
        1:'Dushanba',
        2:'Seshanba',
        3:'Chorshanba',
        4:'Payshanba',
        5:'Juma',
        6:'Shanba',
        7:'Yakshanba'
       }
    kun = int(input('hafta kunini kiriting-->'))
    if kun < 8 and kun > 0:
        print(hafta[kun])
    else:
        print("1 va 7 oralag'idagi sonni kiriting")

'''






'''
hafta = {
        1:'Dushanba',
        2:'Seshanba',
        3:'Chorshanba',
        4:'Payshanba',
        5:'Juma',
        6:'Shanba',
        7:'Yakshanba'
       }
while True:
    import random
    son = int(input('tasoddifiy hafta kunini toping-->'))
    tasoddifiy_son = random.randint(1, 7)
    print('siz tanlagan hafta kuni -->', hafta[son])
    print('tasoddifiy hafta kuni -->',hafta[tasoddifiy_son])
    if son == tasoddifiy_son:
        print('Ura siz topdingiz !!!')
    else:
        print("Afsuski yana birbor urinib ko'ring !!!")


#   kelgusi darsda ismlarni va tel raqamlarni random qilamiz

'''


'''
import random

while True:
            #0              1           2           3          4
    tel =['904154445','334154445','914516289','884561258', '998745623']
    tasoddifiy_son = random.randint(0, len(tel)-1)
    print(tel[tasoddifiy_son])
    print('son -->',tasoddifiy_son)
    x = input('agar davom ettirishni xoxlasangiz Enter ni bosing!!!')

'''

































import hashlib


parol2 = input('parolni kiriting -->')

hashed_parol2 = hashlib.sha256(parol2.encode()).hexdigest()
#print(parol2)
#print(hashed_parol2)

#parol = 'salom12'
#hashed_parol = hashlib.sha256(parol.encode()).hexdigest()

baza_parol = 'b23df8535e1442ff38495728b55ff2afabf91ff3f8ef7c3ee1e4ecad0b36e79e'
#print('bizning parol ', hashed_parol)

if hashed_parol2 == baza_parol:
    print("parol to'g'ri")
    print(hashed_parol2)
    print(baza_parol)
else:
    print("parol xato xxxxxx")
    print(hashed_parol2)
    print(baza_parol)























