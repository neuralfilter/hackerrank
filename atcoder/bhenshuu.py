l = map(int, raw_input().split())
arr = [0]*(l[0])
temp = [map(int, raw_input().split()) for i in range(l[1])]
for x in range(len(temp)):
    for t in range(temp[x][0]-1, temp[x][1]):
        arr[t] = temp[x][2]

for g in range(len(arr)):
    print arr[g]
