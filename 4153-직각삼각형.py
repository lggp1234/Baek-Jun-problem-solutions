D=True
while D:
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print("right")
    else:
        print("wrong")
