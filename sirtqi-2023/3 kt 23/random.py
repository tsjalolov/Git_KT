import random
while True:
    
    a = int(input("qiz bolalar o'ylagan son >> "))
    d = int(input("o'g'il bolalar o'ylagan son >> "))
    b = random.randint(1,3)
    if a == b:
        print('uraaa qiz bolalar topdi')
    elif d == b:
        print("uraaa o'g'il bolalar topdi")
    else:
        print("yana birbor urinib ko'ring", b)
