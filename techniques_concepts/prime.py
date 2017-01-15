def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

p = int(input().strip())
for _ in range(p):
    n = int(input().strip())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
