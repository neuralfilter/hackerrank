numb = [map(int, raw_input().split()) for i in xrange(int(raw_input()))]

numb.sort()

for i in range(len(numb)):
    if numb[i][1] < numb[i][0]:
        print "Happy Alex"
        exit()

print "Poor Alex"
