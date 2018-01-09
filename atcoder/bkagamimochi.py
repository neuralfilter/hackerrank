l = int(raw_input())
arr = []
for i in range(l):
    s = raw_input()
    arr.append(s)
arr = sorted(arr, reverse=True)
counter = 1
for s in range(1,len(arr)):
    if arr[s] < arr[s-1]:
        counter+=1

print counter
