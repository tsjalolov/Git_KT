#   1   10  2 * 1 = 2
#           2 * 2 = 4
while True:
    n =  int(input('n = '))
    for i in range(1, 10+1,1):
        p = i * n
        print(n,'*',i,'=', p)
