from collections import defaultdict

def ransom_note(magazine, ransom):
    word_count = defaultdict(lambda: 0)
    for m in magazine:
        word_count[m] += 1
    for r in ransom:
        word_count[r] -= 1
        if word_count[r] < 0:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
