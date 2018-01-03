import sys
sys.getrecursionlimit()
sys.setrecursionlimit(100000)

l = int(raw_input())

def factorial(l):
    if l == 0:
        return 1
    else:
        return l * factorial(l-1)
integ = factorial(l)
integ = integ
factors = []
i = 1

while(integ >= i):
    if (integ % i) == 0:
        factors.append(i)
    i+=1
print len(factors)
divisor = long(len(factors))
origin =long((10 ** 9) + 7)
