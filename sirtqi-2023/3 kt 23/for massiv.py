'''for i in range(1,10+1,1):
    for j in range(1,10+1,1):
        p = i * j
        print(i,'*',j,'=',p)
        
    #print('2','*',i,'=',p)'''
def salom(x):
    import time
    for i in range(1,x+1,1):
        print('salom',i)
        time.sleep(3)
    
def kara(x):
    for i in range(1,10+1,1):
        p = i * x
        print(x,'*',i,'=',p)
