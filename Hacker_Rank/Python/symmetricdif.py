ignore = raw_input()
k = set(map(int, raw_input().split()))
ignore = raw_input()
l = set(map(int, raw_input().split()))
arr = (list(k.difference(l)))
arr = arr + (list(l.difference(k)))
arr.sort()
for i in range(len(arr)):
    print arr[i]
