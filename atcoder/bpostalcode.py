l = map(int, raw_input().split())
k = raw_input()
listed = list(k)
if (len(k) == (l[0] + l[1] + 1)) and (listed[l[0]] == "-"):
    if (str("".join(listed[0:l[0]])).isdigit() == True) and (str("".join(listed[l[0]+1:len(listed)])).isdigit() == True):
        print "Yes"
        exit()
    print "No"
else:
    print "No"
