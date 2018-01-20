arr = []
sap = [int(raw_input()) for i in range(int(raw_input()))]
for i in range(len(sap)):
    h = 1
    for x in range(sap[i]):
        if x % 2 == 0:
            h *= 2
        elif (x % 2 == 1):
            h += 1
    arr.append(h)

for i in range(len(arr)):
    print arr[i]
