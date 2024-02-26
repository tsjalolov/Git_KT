olmaKg = int(input("necha kg olma oldiz -->"))
olmaNarx = int(input("1 kg olma narxi -->"))
olmaUmumiyQiymati = olmaKg * olmaNarx
olmaSkidka = olmaUmumiyQiymati /100 *15
tulov = olmaUmumiyQiymati - olmaSkidka
if olmaKg >= 10:
    print('boooom sizga coca cola chiqdi')
print("sizning umumiy xaridingiz -->",\
      olmaUmumiyQiymati)
print('sizning chegirmangiz =',olmaSkidka)
print("To'lashingiz kerak --> ",tulov)
