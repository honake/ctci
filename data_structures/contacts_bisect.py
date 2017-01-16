import bisect
n = int(input().strip())
contacts = []

for _ in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        bisect.insort_left(contacts, contact)

    if op == 'find':
        left = bisect.bisect_left(contacts, contact)
        prefix_next = contact[:-1] + chr(ord(contact[-1]) + 1)
        right = bisect.bisect_left(contacts, prefix_next)
        print(right - left)
