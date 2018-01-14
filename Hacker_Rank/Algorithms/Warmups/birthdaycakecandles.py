ignore = raw_input()

k = map(int, raw_input().split())
k.sort()
print k.count(max(k))
