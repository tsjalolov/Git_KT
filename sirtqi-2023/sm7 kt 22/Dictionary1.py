

def hafta(son_hafta):
    hafta = {
        1 : 'dushanba',
        2 : 'seshanba',
        3 : 'chorshanba',
        4 : 'payshanba',
        5 : 'juma',
        6 : 'shanba',
        7 : 'yakshanba'    
        }
    if son_hafta > 7 or 1 > son_hafta:
        print('hafta kunni xato kiritdiz ')
    else:
        print(hafta[son_hafta])

hafta(4)

import datetime
import time
i = 0
while True:    
    x = datetime.datetime.now()
    print(x)
    time.sleep(2)
    i = i + 1
    if i == 10:
        break











'''#    salom : hellow
mashina1 = {
    'salom' : 'hellow',
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
mashina2 = {
    'salom' : 'hellow',
    "brand": "chevrolet",
    "model": "cobalt",
    "year": 2023
    }
print('----> ',mashina2['model'])
#print(lugat)

#print('----> ',lugat['salom'])'''



            
