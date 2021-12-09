shape=[]
def star(n,row,col):
    if n==0:
        shape[0][0]='*'
        return
    if n==3:
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    shape[row+i][col+j]=' '
                else:
                    shape[row+i][col+j]='*'
    else:
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    star(n//3,row+i*(n//3),col+j*(n//3))
    return

n=int(input())
for i in range(n):
    shape.append([])
    for j in range(n):
        shape[i].append(' ')

star(n,0,0)

for i in range(n):
    print(''.join(shape[i]))