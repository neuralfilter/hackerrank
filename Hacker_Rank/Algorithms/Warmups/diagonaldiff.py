j = int(raw_input())
k = [map(int, raw_input().split()) for xaxis in xrange(j)]
leftsum = 0
rightsum = 0

for i in xrange(len(k)):
    rightsum += k[i][len(k)-i-1]
    leftsum += k[i][i]

print abs((leftsum)-(rightsum))
