while True:
    a = int(input('a = '))
    b = int(input('b = '))
    c = a + b
    print('a + b = ',c)
    if a > b:
        print('a katta')
    else:
        if a == b:
            print('a = b')
        else:
            print('b katta')
