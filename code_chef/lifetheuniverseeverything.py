
k = []
counter = 0
while(True):
    temp = int(raw_input())
    if temp == 42:
        break
    elif counter == 0:
        k.append(temp)
for i in xrange(len(k)):
    print k[i]
