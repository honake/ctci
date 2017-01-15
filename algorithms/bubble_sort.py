n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
swaps = 0
flag = True

while flag:
    flag = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swaps += 1
            flag = True

print("Array is sorted in {0} swaps.".format(swaps))
print("First Element: {0}".format(arr[0]))
print("Last Element: {0}".format(arr[-1]))
