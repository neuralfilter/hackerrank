import sys
sys.setrecursionlimit(10000)


l = map(int,raw_input().split())

candcount = int(l[0])
candlehours = 0
leftovers = 0

def recycle(arr, candcount, candlehours, leftovers):
    if candcount < l[0]:
        print candcount
        candlehours += candcount
        print candlehours
        leftovers += candcount
        lefttime = (leftovers) % l[1]
        return (candcount + candlehours) + ((leftovers) / l[1]) + lefttime
    else:
        candlehours += candcount
        if (candcount % l[1] > 0):
            leftovers+=(candcount % l[1])
            return recycle(arr, ((candcount - (candcount % l[1]))/l[1]), candlehours, leftovers)
        elif candcount % l[1] == 0:
            candcount = candcount / l[1]
            return recycle(arr, candcount, candlehours, leftovers)


print recycle(l, candcount, candlehours, leftovers)
