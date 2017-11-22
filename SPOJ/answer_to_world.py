num = 0
arr = []
while(True):
    x = input()
    if(x == 42):
        break
    arr.append(x)
    num += 1

for i in arr:
    print(i)
