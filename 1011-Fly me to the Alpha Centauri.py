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

# 최고점이 M이라면
# 숫자 L=M^2 ~ M^2-M+1 -> 2M-1을 길이로 가짐. 루트L을 반올림 하면 M이됨.
# 숫자 L=M^2 ~ M^2+M -> 2M를 길이로 가짐. 루트L을 반올림 하면 M이됨