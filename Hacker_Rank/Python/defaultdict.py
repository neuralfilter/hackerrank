from collections import defaultdict

k = map(int, raw_input().split())
unique = set()

d = defaultdict(list)
for i in range(k[0]):
    list1 = str(raw_input())
    d[list1].append(i+1)
    unique.add(list1)

unique = list()
for x in range(k[1]):
    list2 = str(raw_input())
    unique.append(list2)


for i in unique:
    if i in d:
        print " ".join(map(str, d[i]))
    elif i not in d:
        print -1
