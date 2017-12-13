def front_times(str, n):
    liststr = list(str)
    listed = []
    if(len(str)>=3):
        front = ''.join(liststr[0:3])
        for i in range(n):
            listed.append(front)
        return ''.join(listed)
    elif(len(str)<3):
        front = ''.join(liststr[0:len(str)])
        for i in range(n):
            listed.append(front)
        return ''.join(listed)
