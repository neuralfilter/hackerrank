from itertools import combinations

l = list(map(int, raw_input().split()))
listed = []
for var in combinations(l, 3):
    listed.append(var[0] + var[1] + var[2])
print listed
temp = []

for i in range(len(listed)):
    for x in xrange(len(listed)):

    if listed[i] not in temp:
#print temp
#print listed

if (len(temp) > len(listed)) or (len(listed) > len(temp)):
    print "YES"
elif (len(temp) == len(listed)):
    print "NO"
