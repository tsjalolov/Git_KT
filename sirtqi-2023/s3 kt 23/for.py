# S = 1 + 2 + 3 +...+ 10
#print('nechi sonigacha bo`lgan sonlarning juftlarini yig`indisini chiqaray')
x = int(input('sonni kiriting = '))
print('agar juft yig`indi bo`lsa  1 ')
print('agar toq yig`indi bo`lsa  2 ')
print('agar hamma sonlar yig`indi bo`lsa  3 ')
y  =  int(input('kiriting >>>'))
S = 0

if y == 1:
    for i in range(2,x+1,2):
        s1 = S
        S = S + i
        print('i = ',i,' S = ',s1,'+',i)
elif y == 2:
    for i in range(1,x+1,2):
        s1 = S
        S = S + i
        print('i = ',i,' S = ',s1,'+',i)
elif y == 3:
    for i in range(1,x+1,1):
        s1 = S
        S = S + i
        print('i = ',i,' S = ',s1,'+',i)
    


print(S)
