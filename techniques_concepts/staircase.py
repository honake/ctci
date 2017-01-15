tb = {1:1,2:2,3:4}

def patterns(n):
    if not n in tb.keys():
        tb[n] = patterns(n - 1) + patterns(n - 2) + patterns(n - 3)
    return tb[n]

s = int(input().strip())

for _ in range(s):
    n = int(input().strip())
    print(patterns(n))
