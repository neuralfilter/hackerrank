l = list(raw_input())
uniquelist = []
for i in range(len(l)):
    if l[i] not in uniquelist:
        uniquelist.append(l[i])
if len(uniquelist) % 2 == 0:
    print "CHAT WITH HER!"
else:
    print "IGNORE HIM!"
