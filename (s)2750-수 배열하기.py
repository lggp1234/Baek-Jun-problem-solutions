#https://www.acmicpc.net/problem/2750
N=int(input())
L=[]
for i in range(N):
    L.append(int(input()))
for i in range(N):
    for j in range(i+1,N):
        if L[i]<L[j]:
            pass
        elif L[i]>L[j]:
            L[i], L[j]=L[j],L[i]
for i in range(N):
    print(L[i])