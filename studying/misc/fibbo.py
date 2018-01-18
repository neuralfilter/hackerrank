import sys
sys.setrecursionlimit(10000)

k = int(raw_input())
arr = [-1]*(k+1)


def fib(k):
    if arr[k] != -1:
        return arr[k]
    elif (k == 1) or (k == 2):
        temp =  1
    elif (k == 0):
        temp = 0
    else:
        temp = fib(k-1) + fib(k-2)
    arr[k] = temp
    return temp


print fib(k)
