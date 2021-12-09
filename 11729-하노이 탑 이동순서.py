def HanoiMove(n,a,b,c):
    if n==1:
        move.append([a,c])
    else:
        HanoiMove(n-1,a,c,b)
        move.append([a,c])
        HanoiMove(n-1,b,a,c)

def HanoiNumb(n):
    if n==1:
        return 1
    else:
        return 2*HanoiNumb(n-1)+1

move=[]

n=int(input())
HanoiMove(n,1,2,3)
print(HanoiNumb(n))
print("\n".join([' '.join(str(i) for i in row) for row in move]))