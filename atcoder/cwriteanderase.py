from collections import Counter

count = int(raw_input())
k = [int(raw_input()) for i in xrange(count)]
temp = Counter(k)
counter = 0
for key, value in temp.iteritems():
    if value % 2 != 0:
        counter += 1

print counter
