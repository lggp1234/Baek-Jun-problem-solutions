#https://www.acmicpc.net/problem/1436
N=int(input())
num=1
while True:
    if '666'in str(num):N-=1
    if N==0:
        break
    num+=1
print(num)