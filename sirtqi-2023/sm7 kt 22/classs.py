'''import math
x = math.pi
y = math.sqrt(25)
print('pi =',x)
print('y =',y)    
                 

def my_pi():
    p = 3.141592653589793
    return(p)
x = my_pi()
#print(x)

def kupaytirish(x,y):
    c = x * y
    return(c)

a = int(input('a ='))
b = int(input('b ='))
x = kupaytirish(a,b)
print(x)'''

def kupaytir(n):
    for i in range(1, 10+1, 1):
        p = n * i
        print(n,'*',i,'=',p)
    print('-------------')
kupaytir(2)
kupaytir(3)
kupaytir(4)
kupaytir(5)
kupaytir(6)























