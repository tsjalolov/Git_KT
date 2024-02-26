S = 0
N = int(input('N = '))

for a in range(1,N+1,1):
    if a == 5:
        print('5 ni olmayman')
        continue
    else:
        print('S = ',S,' + ',a)
        S = S + a
    
    
print(' S = ',S)
    
    
