k = map(int, raw_input().split())
temp = [k[0]]
for i in xrange(1000):
    if sum(temp) % k[1] == k[2]:
        print "YES"
        exit()
    temp.append(int(k[0]))

print "NO"


