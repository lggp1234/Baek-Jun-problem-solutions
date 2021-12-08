N=int(input())
Max=N//5
AnsList=[]
List=[]

for i in range(Max+1):
    n=N-5*i
    if n%3==0:
        a=[n/3,i]
        List.append(a)
    else:
        pass

if len(List)==0:
    print(-1)
else:
    for j in range(len(List)):
        AnsList.append(List[j][0]+List[j][1])
    print(round(min(AnsList)))