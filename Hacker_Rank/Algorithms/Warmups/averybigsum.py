def aVeryBigSum(n, ar):
    arr = [0]*n
    summ = 0
    for i in range(len(ar)):
        summ = long(summ) + long(ar[i])
    return long(summ)
