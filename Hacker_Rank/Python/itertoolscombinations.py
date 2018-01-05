from itertools import combinations

l = map(str, raw_input().split())
listed = list(l[0])
listed.sort()
for i in range(1,int(l[1])+1):
        combos = list(combinations(listed,i))
        for x in range(len(combos)):
            print "".join(combos[x])
