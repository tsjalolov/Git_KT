# salom so'zini 10 marotaba ekranga
#chiqarish
# 1 2 3 ....N-1   N
N = int(input('sonni kiriting ='))
S = 0
for i in range(1,N + 1,1):
    print('S = ',S,' + ',i)
    S = S + i
    
print(S)
