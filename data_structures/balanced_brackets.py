def is_matched(expression):
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    for char in expression:
        if char in pairs.keys():
            stack.append(pairs[char])
        else:
            # You need to check if the stack is empty or not before
            # accessing the last element in it, otherwise you get
            # IndexError: list index out of range
            if stack == [] or char != stack[-1]:
                return False
            stack.pop()
    return (stack == [])

t = int(input().strip())

for _ in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
