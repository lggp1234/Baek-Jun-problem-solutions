#https://www.acmicpc.net/problem/1018
N,M=map(int, input().split())
L=[[]*M]*N
for i in range(N):
    L[i]=list(input())

def D(x,y):
    good1,bad1=0,0
    good2,bad2=0,0
    for a in range(x,x+8):
        for b in range(y,y+8):
            # WBWBWBWB 의 경우 테스트
            if a%2==0 and b%2==0:
                if L[a][b]=='W':
                    good1+=1
                else:
                    bad1+=1
            elif a%2==0 and b%2==1:
                if L[a][b]=='B':
                    good1+=1
                else:
                    bad1+=1
            elif a%2==1 and b%2==0:
                if L[a][b]=='B':
                    good1+=1
                else:
                    bad1+=1
            elif a%2==1 and b%2==1:
                if L[a][b]=='W':
                    good1+=1
                else:
                    bad1+=1
            # BWBWBWBW 의 경우 테스트
            if a%2==0 and b%2==0:
                if L[a][b]=='B':
                    good2+=1
                else:
                    bad2+=1
            elif a%2==0 and b%2==1:
                if L[a][b]=='W':
                    good2+=1
                else:
                    bad2+=1
            elif a%2==1 and b%2==0:
                if L[a][b]=='W':
                    good2+=1
                else:
                    bad2+=1
            elif a%2==1 and b%2==1:
                if L[a][b]=='B':
                    good2+=1
                else:
                    bad2+=1
    if good1>good2:
        return bad1
    else:
        return bad2
            
                
A=[]
for i in range(N-7):
    for j in range(M-7):
        A.append(D(i,j))
print(min(A))