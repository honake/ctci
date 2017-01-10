import string
from collections import defaultdict

def number_needed(a, b):
    steps = 0
    cnt_a, cnt_b = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for p in list(a):
        cnt_a[p] += 1
    for q in list(b):
        cnt_b[q] += 1
    for char in list(string.ascii_lowercase):
        steps += abs(cnt_a[char]-cnt_b[char])
    return steps

a = input().strip()
b = input().strip()

print(number_needed(a, b))
