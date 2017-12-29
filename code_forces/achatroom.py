l = list(raw_input())
checkh = list("hello")
for i in range(len(l)):
    if len(checkh) == 0:
        print "YES"
        exit()
    if l[i] == checkh[0]:
        del checkh[0]
if len(checkh) == 0:
    print "YES"
else:
    print "NO"
