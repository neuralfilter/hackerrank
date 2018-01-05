x, y, num = map(int, raw_input().split())
for i in range(num):
    inputt = map(int, raw_input().split())
    if inputt[2] == 1:
        x = x - inputt[0]
        if y - inputt[1] < 0:
            print 0
            exit()
    elif inputt[2] == 2:
        x =(x - (x - inputt[0]))
        if y - inputt[1] < 0:
            print 0
            exit()
    elif inputt[2] == 3:
        y = y - inputt[1]
        if y - inputt[1] < 0:
            print 0
            exit()
    elif inputt[2] == 4:
        if y - inputt[1] < 0:
            print 0
            exit()
        y = (y - (y - inputt[1]))

    print x,y
if x*y < 0:
    print 0
else:
    print x*y
