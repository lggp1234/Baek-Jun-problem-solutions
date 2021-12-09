s,e=map(int, input().split())
arr=[i for i in range(0,e+1)]

def createPrimeNumber(s,e):
    for i in range(2,e+1):
        if arr[i]==0:
            continue
        if arr[i]%i==0:
            j=2
            while i*j<=e:
                arr[i*j]=0
                j+=1
                
createPrimeNumber(s,e)
for i in range(s,e+1):
    if arr[i]!=0 and arr[i]!=1:
        print(arr[i])