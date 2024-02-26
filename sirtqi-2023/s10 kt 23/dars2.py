olma_narx = int(input('olma narxi => '))
anor_narx = int(input('anor narxi => '))
olma_kg = int(input('olma kg => '))
anor_kg = int(input('anor kg => '))
olma = olma_narx * olma_kg   #100
olma_s = olma * 90 / 100
anor = anor_narx * anor_kg
anor_s = anor * 85 / 100
c = olma_s + anor_s
ekanom = anor - anor_s + olma - olma_s
print("to'lovga -->",c)
print('siz ekanom qildiz ',ekanom )








'''c = a + b
d = c + 5 - 4
print('c = ',c)
print('d = ',d)'''
