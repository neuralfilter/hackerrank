N = input()
a = [raw_input() for i in range(N)]
counter = 0
for i in range(len(a)):
    for x in range(0,len(a[i])-1):
        if (a[i][x:x+2] == "++"):
            counter+=1
        if (a[i][x:x+2] == "--"):
            counter+=-1
print counter
