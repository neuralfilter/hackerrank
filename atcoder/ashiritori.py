l = map(str, raw_input().split())
for i in range(len(l)-1):
    tempa = list(l[i])
    tempb = list(l[i+1])
    if tempa[len(tempa)-1] != tempb[0]:
        print "NO"
        exit(0)
print "YES"
