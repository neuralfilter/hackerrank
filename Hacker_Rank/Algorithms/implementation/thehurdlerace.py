k = map(int, raw_input().split())
l = map(int, raw_input().split())
counter = 0

if max(l) > k[1]:
    print max(l) - k[1]
else:
    print 0
#for i in range(1,len(l)):
#    if (l[i]) > k[1]:
#        counter += 1

