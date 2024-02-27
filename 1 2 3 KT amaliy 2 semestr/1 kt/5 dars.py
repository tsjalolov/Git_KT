'''n = int(input('n = '))
#x = n % 2 == 0
#print('n = ',n,'--> ',x)
if n % 2 == 0:
    print('n = ',n,'--> ','juft son')
else:
    print('n = ',n,'--> ','toq son')'''

'''a = int(input('a = '))
#x = a < 0
#print('a = ',a,'--> ',x)
if a < 0:
    print('a = ',a,'--> ','manfiy son')
else:
    print('a = ',a,'--> ','musbat son')'''














a = int(input('a = '))
b = int(input('b = '))

if a < 0 and b < 0:
    print('a = ',a,'--> ','manfiy son')
    print('b = ',b,'--> ','manfiy son')
elif a > 0 and b < 0:
    print('a = ',a,'--> ','musbat son')
    print('b = ',b,'--> ','manfiy son')
elif a < 0 and b > 0:
    print('a = ',a,'--> ',' manfiy son')
    print('b = ',b,'--> ','musbat son')
elif a > 0 and b > 0:
    print('a = ',a,'--> ',' musbat son')
    print('b = ',b,'--> ','musbat son')
else:
    print('nol aralashgan')

