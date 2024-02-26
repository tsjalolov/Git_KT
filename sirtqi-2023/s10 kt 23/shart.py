a = int(input('a = '))
b = int(input('b = '))

if a > b:
    c = a - b
    print('a katta',c,'ta ga')
else:
    if a == b:
         print('a=b ga')
    else:
        c = b - a
        print('b katta',c,'ta ga')
