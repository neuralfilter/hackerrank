def string_match(a,b):
    alist = list(a)
    blist = list(b)
    dic = []
    counter = 0
    for i in range(len(a)-1):
            print b[i:i+2]
            if ((a[i:i+2]) == (b[i:i+2]) and (a[i:i+2] not in dic)):
                dic.append(a[i:i+2])
    return len(dic)
