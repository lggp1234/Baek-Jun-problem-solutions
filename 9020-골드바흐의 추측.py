def NewErato(n,Ans):
    prime=[True]*n
    for k in range(2,int(n**0.5)+1):
        if prime[k]:
            for i in range(k*k, n, k):
                prime[i]=False
    for i in range(len(prime)):
        if prime[i]==True:
            Ans.append(i)
        else:
            pass
    Ans.remove(0)
    Ans.remove(1)
    return Ans

def GoldBach(n):
    li=NewErato(n,[])
    idx=max([i for i in range(len(li)) if li[i]<=n/2])
    for i in range(idx,-1,-1):
        for j in range(i,len(li)):
            if li[i]+li[j]==n:
                return [li[i],li[j]]

T=int(input())
for tc in range(T):
    n=int(input())
    P=NewErato(n,[])
    print(" ".join(map(str,GoldBach(n))))