from collections import Counter

k = list(raw_input())
counted = Counter(k)
for key, value in counted.iteritems():
    if value > 1:
        print "no"
        exit()

print "yes"
