from itertools import combinations

k = map(int, raw_input().split())
n = map(int, raw_input().split())
counter = 0
arr = list(combinations(n, 2))
for i in range(len(arr)):
    if sum(arr[i]) % int(k[1]) == 0:
        counter += 1

print counter
#[i for i in range(len(arr))]
