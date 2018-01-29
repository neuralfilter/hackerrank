lights = [int(raw_input()) for i in xrange(int(raw_input()))]
lamps = [0]*len(lights)
lamps[0] = 1
for i in xrange(len(lamps)):
    if (i > 0):
        lamps[int(lights[i])-1] += 1
    if lamps[1] == 1:
        print i
        exit()
    print lamps
print -1
