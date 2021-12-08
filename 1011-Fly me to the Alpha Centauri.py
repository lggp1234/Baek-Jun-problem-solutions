import math
T=int(input())
for a in range(T):
    x,y=map(int, input().split())
    d=y-x
    k=round(math.sqrt(d))
    if d>k**2:
        print(2*k)
    else:
        print(2*k-1)