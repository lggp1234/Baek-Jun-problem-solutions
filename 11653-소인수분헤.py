import math

def PrimeDis(i):
    d=0
    if i==1:
        return 0
    for k in range(1,math.floor(math.sqrt(i))+1):
        if i%k==0:
            d+=1
        else:
            pass
    if d==1:
        return 1
    else:
        return 0
    
N=int(input())
d=0
while N>1:
    d+=1
    if PrimeDis(N)==1:
        print(round(N))
        break
    if PrimeDis(d)==1:
        D=True
        while D:
            if N%d==0:
                N=N/d
                print(d)
            else:
                D=False
    else:
        pass