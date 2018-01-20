ignore = int(raw_input())
counter = [0]*6

for i in map(int, raw_input().split()):
    counter[i] += 1
print counter.index(max(counter))
