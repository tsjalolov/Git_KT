#sqrt
'''from math import *
a = float(input('a = '))
b = float(input('b = '))
c = sqrt(pow(a,2) + b**2)
print(c)'''
'''a = float(input('a = '))
print('pow(a,2) -->',pow(a,2))
print('pow(a,3) -->',pow(a,3))
print('pow(a,9) -->',pow(a,9))'''
skidka = 10
k_summ = float(input('1 kg konfet narxi = '))
k_kg = float(input('konfet kg sini kiriting = '))
u_summ = k_summ * k_kg
s_10 = u_summ * skidka / 100
print('umumiy summa ',u_summ,"so'm")
print(skidka, '% skidka sizga ',s_10,"so'm")
tulov = u_summ - s_10
print("kassaga to'lov --> ",tulov,"so'm")
