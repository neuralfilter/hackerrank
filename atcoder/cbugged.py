q = int(raw_input())
arr = []
for i in range(q):
    arr.append(int(raw_input()))

if sum(arr) % 10 != 0:
    print sum(arr)
    exit()

arr = sorted(arr)

for x in range(len(arr)):
    if (sum(arr[x:] + arr[:x+1]) % 10 != 0):
        print sum(arr[:x] + arr[x+1:])
        exit()

print 0
