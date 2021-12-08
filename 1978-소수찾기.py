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

def PrimeL(i):
    PrimeList=[]
    for j in range(1,i+1):
        if PrimeDis(j)==1:
            PrimeList.append(i)
        else:
            pass
    return PrimeList
        

N=int(input())
Test=[]
Test.append(list(map(int, input().split())))

PrimeList=[]
for i in range(1,1001):
    if PrimeDis(i)==1:
        PrimeList.append(i)
    else:
        pass

s=0
for j in Test[0]:
    D=PrimeList.count(j)
    if D!=0:
        s+=1
    else:
        pass
    
print(s)