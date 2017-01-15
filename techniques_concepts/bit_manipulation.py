def lonely_integer(a):
    res = 0
    for e in a:
        res ^= e
    return res

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
