while True:
    olmaKg = int(input('necha kg olma oldiz--> '))
    olmaNarx = int(input('1 kg olma narxi --> '))
    olmaUmumiySum = olmaKg * olmaNarx
    skidka15 = olmaUmumiySum / 100 * 15
    tulov = olmaUmumiySum - skidka15
    print('sizning xaridingiz--> ',olmaUmumiySum)
    print('siz tejagan summa--> ',skidka15)
    print("to'lovga -->",tulov)
    if olmaKg >= 10:
        print('sizga pepsi bonusga chiqdi')
    else:
        if olmaKg >= 5:
            print('sizga fanta bonusga chiqdi')
        else:
            print('sizga snekers bonusga chiqdi')
