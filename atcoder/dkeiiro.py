import sys
sys.setrecursionlimit(500000)
modnum = 10**9+7
N, M = map(int, raw_input().split())
a = [map(int, raw_input().split()) for xaxis in xrange(N)]

memo = [[0] * M for _ in xrange(N)]


def dfs(x, y, xmax, ymax, a, modnum, memo):
    if (memo[x][y] > 0):
        return memo[x][y]
    elif (memo[x][y] == 0):
        checked = 1
        xy_val = a[x][y]
        temps = [0, -1, 0, 1, 0]
        for i in xrange(4):
                ai = x + temps[i]
                aj = y + temps[i+1]
                if (0 <= ai < N) and (0 <= aj < M) and (xy_val < a[ai][aj]):
                    checked += dfs(ai, aj, N, M, a, modnum, memo) % modnum
        memo[x][y] = checked
    return memo[x][y]


sums = 0
for x in xrange(N):
    for y in xrange(M):
        sums += dfs(x, y, N, M, a, modnum, memo)
print sums % modnum
