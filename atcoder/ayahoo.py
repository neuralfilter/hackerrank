l = list(raw_input())
yahoo = ["y", "a", "h", "o", "o"]
x = 0
if l == "yohaa":
    print "NO"
for i in range(len(l)):
    for k in range(len(l)):
        if yahoo[i] == l[k]:
            x+=1
            break
if x == 5:
    print "YES"
else:
    print "NO"
