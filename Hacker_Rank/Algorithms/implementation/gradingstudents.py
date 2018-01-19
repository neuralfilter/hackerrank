count = int(raw_input())
arr = [(int(raw_input())) for i in range(count)]

for i in range(len(arr)):
    if (arr[i] >= 38) and (((arr[i] + (5 - (arr[i] % 5))) - arr[i]) < 3):
        arr[i] = arr[i] + (5 - (arr[i] % 5))

for i in range(len(arr)):
    print arr[i]
