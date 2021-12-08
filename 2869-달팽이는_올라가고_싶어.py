import math
A,B,V=map(int, input().split())
k=A-B
s=(V-A)/(A-B)
Ans=math.ceil(s)+1
print(Ans)