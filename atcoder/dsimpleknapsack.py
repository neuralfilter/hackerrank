import sys
sys.setrecursionlimit(10000)

k = map(int, raw_input().split())

item = [map(int, raw_input().split()) for x in xrange(k[0])]
memo = [[0]*int(k[1]+1) for i in xrange(k[0]+1)]


def knapsack(items, capacity):
    for i in range(k[1]+1):
        for n in range(k[0]+1):
            if items == 0 or capacity == 0:
                memo[i][n] = 0
            else:
                memo[i][n] = memo[i-1][n]
    return memo[i][n]

knapsack(item[0], item[1])
print memo
