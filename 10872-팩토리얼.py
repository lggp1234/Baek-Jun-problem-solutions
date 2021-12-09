def Factorial(n):
    if n<=1:
        return 1
    else:
        return Factorial(n-1)*n

print(Factorial(int(input())))