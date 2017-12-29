l = int(raw_input())
strings = []
i = 0
if l == 1:
    print "I hate it"
    exit()
while l >= i:
    if i % 2 == 0:
        strings.append("I hate")
        i+=1
        if l == i:
            break
        strings.append("that")
#        elif (i) == l:
#            strings.append("it")
#            break
    if i % 2 == 1:
        strings.append("I love")
        i+=1
        if l == i:
            break
        strings.append("that")
#        elif (i) == l:
#            strings.append("it")
#            break
print ' '.join(strings) + " it"
