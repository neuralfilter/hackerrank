l = map(int,raw_input().split())
new = []
for i in range(l[0]+1):
    temp = map(int, str(i))
    total = sum(temp)
    if (l[1] <= total <= l[2]):
        new.append(i)
print sum(new)
