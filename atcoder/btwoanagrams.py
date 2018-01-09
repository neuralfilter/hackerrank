l = list(str(raw_input()))
k = list(str(raw_input()))

l.sort()
l = "".join(l)
k = sorted(k, reverse=True)
k = "".join(k)

if l < k:
    print "Yes"
else:
    print "No"
