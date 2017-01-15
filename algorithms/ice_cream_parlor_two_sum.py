def two_sum(m, n, a):
    tb = {}
    for idx, val in enumerate(a):
        if m - val in tb:
            print("{0} {1}".format(tb[m - val] + 1, idx + 1))
        else:
            tb[val] = i

t = int(input().strip())
for _ in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    two_sum(m, n, a)
