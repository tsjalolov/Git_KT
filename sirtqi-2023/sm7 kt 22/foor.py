# for
'''a = int(input('a = '))
for i in range(1,a+1,1):
    if i == 5:
        print("besh sonida to'xtayman")
        break
    print(i)'''
    
'''a = int(input('a = '))
for i in range(1,a+1,1):
    if i == 5:
        print('besh sonini chiqarmayman')
        continue
    print(i)'''
    
'''s = 'salom'
for i in s:
    if i == 'a':
        continue
    print(i)'''
# while

'''a = 1
while a <= 7:
    print(a)
    a = a + 1'''
#random       b = 6 integer(int)     c = 6,7    float
'''
import random
while True:    
    a = random.randint(5,10)
    b = int(input('b = '))
    if a == b:
        print("urra men toptim")
        print(a)
    else:
        print("yana bir bor urinib ko'raman")
        print('tasodifiy sonimiz',a, 'ga teng')
    x = input("yana son kiritasizmi? ha/yo'q ")
    if x != 'ha':
        break
print('dasturimiz tugadi!')'''

# 1 * 1 = 1
# 1 * 2 = 2        2 2 2 2
# 1 * 10 = 10     1 3 5 7 9 

a = int(input('a = '))
for i in range(1, 10 + 1, 1):
    natija = a * i
    
    print(a,'*',i,'=',natija)











    
