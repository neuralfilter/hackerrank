from collections import Counter

input()
k = map(int, raw_input().split())

k = Counter(k)
counted = 0

for key, value in k.items():
    counted += (value - (value % 2)) / 2
print counted
