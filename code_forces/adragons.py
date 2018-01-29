k = map(int, raw_input().split())
power = int(k[0])

array = [map(int, raw_input().split())for i in xrange(k[1])]
array.sort()
for i in xrange(len(array)):
    if power > array[i][0]:
        power += int(array[i][1])
    else:
        print "NO"
        exit()

print "YES"
