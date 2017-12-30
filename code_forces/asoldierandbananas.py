l = map(int,raw_input().split())
cost = 0
for i in range(1,l[2]+1):
    cost = cost + (l[0]*i)

if cost > l[1]:
    print cost-l[1]
else:
    print 0
