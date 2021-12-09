T=int(input())
for t in range(T):
    a,b,m,c,d,n=map(int, input().split())
    x=((a-c)**2+(b-d)**2)**0.5
    if x==0:
        if m==n:
            print(-1)
        else:
            print(0)
    else:
        if x==m+n or x==abs(m-n):
            print(1)
        elif x>abs(m-n) and x<abs(m+n):
            print(2)
        else:
            print(0)