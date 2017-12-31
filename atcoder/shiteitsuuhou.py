l = float(raw_input())
l = float(l) / 1000.0

if  0.1 > l:
    print "00"

elif 0.1 < l < 5:
    l = l*10
    if l < 10:
        print "0" + str(int(l))
    else:
        print int(l)
elif 6 < l < 30:
    print 50 + int(l)

elif 35 < l < 70:
    print int( ( (l - 30.0) / 5.0) + 80.0)

elif  l > 70:
    print "89"
