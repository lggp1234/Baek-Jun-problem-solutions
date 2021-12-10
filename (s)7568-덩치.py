#https://www.acmicpc.net/problem/7568
N=int(input())
x,y=[0]*N,[0]*N
for i in range(N):
    x[i],y[i]=map(int, input().split())
    
def D(a):
    U=0
    for i in range(N):
        if x[a]<x[i] and y[a]<y[i]:
            U+=1
    return U

Ranking=[0]*N
for i in range(N):
    Ranking[i]=D(i)
for i in range(N):
    print(Ranking[i]+1, end=' ')