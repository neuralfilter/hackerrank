k = map(int, raw_input().split())
if (k[2] < k[0]):
    print "delicious"
    exit()
if (k[2]-k[1] <= k[0]):
    print "safe"
else:
    print "dangerous"
