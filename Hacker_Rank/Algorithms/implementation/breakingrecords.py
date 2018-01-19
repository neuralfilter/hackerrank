ignore = int(raw_input())
counter = [0, 0]
k = map(int, raw_input().split())
high = int(k[0])
low = int(k[0])
for i in range(1, len(k)):
    if k[i] < low:
        counter[1] += 1
        low = int(k[i])
    elif k[i] > high:
        counter[0] += 1
        high = int(k[i])

print counter[0],counter[1]
