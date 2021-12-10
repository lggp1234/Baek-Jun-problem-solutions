#https://www.acmicpc.net/problem/2798
N,M=map(int, input().split())
A=[300000]
List=list(map(int, input().split()))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            x=M-List[i]-List[j]-List[k]
            if x<0:
                continue
            elif x<=max(A):
                A[0]=x
print(M-A[0])