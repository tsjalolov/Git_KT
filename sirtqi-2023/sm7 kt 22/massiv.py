'''a = 5           # int (integer)  --> butun son
b = 5.5         # float          --> kasir son

#    01234
c = 'salom, dunyo'     # str  (string)  --> so'z
print("so'z =",c)
print("so'zning tipi =",type(c))
print("so'zning uzunligi =",len(c))       #len uzunlik
print("so'zning [2:10] oralig'i =",c[2:10])
print("so'zning [:10] oralig'i =",c[:10])
print("so'zning [2:] oralig'i =",c[2:])
for i in c:
    if i == 'o':
        print("biz o harfini chop etmaymiz")
        continue
    print(i)'''





#    0 1  2  3  4     5 6
a = [1,11,8,3,4,1,7]
print('tartibsiz ',a)
print('1 dan 4 gacha oraliq --->',a[1:4])
print('a massivning uzunligi --->', len(a))
a.sort()
print('tatiblangan',a)







'''
for i in a:
    if i == 3:
        print('uch raqamini chiqarmayman')
        continue
    print(i)'''





















