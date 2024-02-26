'''a = int(input('sonni kiriting a = '))
b = int(input('sonni kiriting b = '))
c = a + b
d = c/2 + 5 - a
print(d)

a = int(input('mening yilim = '))
b = int(input('sening yiling = '))

if a > b:
    c = a - b
    print('men sendan ', c, ' yosh kichikman')
else:
    if a == b:
        print('bizning yoshimiz teng')
    else:
        c = b - a
        print('sen mendan ', c, ' yosh kichiksan')'''

olma_kg = int(input('olma kg = '))
anor_kg = int(input('anor kg = '))

olma_narxi = int(input('olma narxi = '))
anor_narxi = int(input('anor narxi = '))

olma_summa = olma_kg * olma_narxi
anor_summa = anor_kg * anor_narxi

if olma_summa > anor_summa:
    c =olma_summa - anor_summa
    print('anorga nisbatan', c, ' so`m ko`p xarajat bo`ldi')
else:
    if olma_summa == anor_summa:
        print('olma va anor xarajati  teng')
    else:        
        c =anor_summa - olma_summa
        print('olmaga nisbatan ', c, ' so`m ko`p xarajat bo`ldi')
