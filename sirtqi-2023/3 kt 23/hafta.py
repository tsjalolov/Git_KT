while True:
    a = {
        1:'dushanba',
        2:'seshanba',
        3:'chorshanba',
        4:'payshanba',
        5:'juma',
        6:'shanba',
        7:'yakshanba'    
        }
    b = int(input('sizga qaysi hafta kuni kerak-->'))
    if b > 0 and b < 8:
        print(a[b])
    else:
        print('qayta uruning')

