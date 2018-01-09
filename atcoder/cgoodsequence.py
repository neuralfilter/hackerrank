from collections import Counter

ignore = int(raw_input())
k = dict(Counter(map(int, raw_input().split())))
copyk = list(set(k))
counter = 0
for i,j in k.items():
    if i > j:
        counter += j
    elif i < j:
        counter += j - i

print counter
