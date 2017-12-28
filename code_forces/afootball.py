l = raw_input()
listed = list(l)
if len(l) < 7:
    print "NO"
    quit()
for i in range(len(l)-6):
    if ((''.join(l[i:i+7])) == "0000000") or ((''.join(l[i:i+7])) == "1111111"):
        print "YES"
        quit()
    if i == len(l)-7:
        print "NO"
        quit()
print "NO"
quit()
