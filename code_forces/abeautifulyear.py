l = int(raw_input())
while(True):
    l+=1
    listl = list(str(l))
    for i in range(10):
        if str(i) in listl:
            listl.remove(str(i))
        if len(listl) == 0:
            print l
            exit()
