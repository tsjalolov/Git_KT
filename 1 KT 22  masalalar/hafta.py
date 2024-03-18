#salom github dan
'''while True:
    n = int(input('n = '))
    b = {
        1: 'dushanba',
        2: 'seshanba',
        3: 'chorshanba',
        4: 'payshanba',
        5: 'juma',
        6: 'shanba',
        7: 'yakshanba',
        8: 'hapshanba' 
        }
    if n > 0 and n < 8:
        print(b[n])
    else:
        print(b[8])  '''
'''
while True:
    n = int(input('n ='))
    son = {
        1:'bir xonoli',
        2:'ikki xonoli',
        3:'uch xonoli',
        4:'to`rt xonoli',
        5:'besh xonoli',
        }
    uzunlik = len(str(n))   #3
    if uzunlik in son:
        print(son[uzunlik])
    else:
        print('kechirasiz')
'''
n = int(input('n ='))
birlik = {
    1:'bir',
    2:'ikki',
    3:'uch',
    4:'to`rt',
    5:'besh',
    6:'olti',
    7:'yetti',
    8:'sakkiz',
    9:"to'qqiz",
    0:''
    }
unlik = {
    1:"o'n",
    2:'yigirma',
    3:"o'ttiz",
    4:'qirq',
    5:'ellik',
    6:'oltmish',
    7:'yetmish',
    8:'sakson',
    9:"to'qson",
    0:'',
    }
yuzlik = {
    0:'',
    1:"yuz",
    2:'ming',
    3:"yuzming",
    4:'milion',
    5:'milliard'
    }
suz = str(n)
if len(suz)==1:
    #4
    chiqarish = birlik[int(suz[0])]    
elif len(suz)==2:
    #99
    chiqarish = unlik[int(suz[0])] +' ' + birlik[int(suz[1])]
elif len(suz)==3:
    #999
    chiqarish =birlik[int(suz[0])]  +' ' + yuzlik[1] +' ' + unlik[int(suz[1])] +' ' + birlik[int(suz[2])]
elif len(suz)==4:
    #9999
    if suz[1]==0:
        yuz = ''
    else:
        yuz = yuzlik[1]  
    chiqarish =birlik[int(suz[0])]  +' ' + yuzlik[2] +' ' + birlik[int(suz[1])]  +' ' + yuz +' ' + unlik[int(suz[2])] +' ' + birlik[int(suz[3])]
elif len(suz)==5:
    #99999
    chiqarish =unlik[int(suz[0])] +' ' + birlik[int(suz[1])]  +' ' + yuzlik[2] +' ' + birlik[int(suz[2])]  +' ' + yuzlik[2] +' ' + unlik[int(suz[3])] +' ' + birlik[int(suz[4])]



    
print(chiqarish)



















