def fib(n):
    a,b = 0,1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n-2):
            a,b = b, a+b
        return a+b

n = int(input())
print(fib(n))
