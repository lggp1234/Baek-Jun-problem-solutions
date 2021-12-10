#https://www.acmicpc.net/problem/2231
N=int(input())
def SplitSum(N):
    N=N+sum(map(int, str(N)))
    return N
A=[0]*(1000000+1)
for i in range(1,N+1):
    A[i]=SplitSum(i)
if N not in A:
    print(0)
else:
    for i in range(1,N+1):
        if N==A[i]:
            print(i)
            break
        else:
            pass