l = raw_input()
listedl = list(l)
for i in reversed(range(0,l[2]+1)):
    print i
    if (l[0]*l[1]) % (i*i) == 0:
        print (l[0]*l[1]) / (i*i)
        break
    if (l[0] == 1) or (l[1] == 1):
        print 1
        break
    if l[0]*l[1] < i*i:
        print 1
        break
