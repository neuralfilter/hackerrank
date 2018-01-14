from __future__ import division


def plusMinus():
    ignore = raw_input()
    k = map(int, raw_input().split())
    print(sum(n > 0 for n in k) / len(k))
    print(sum(n < 0 for n in k) / len(k))
    print(sum(n == 0 for n in k) / len(k))

plusMinus()
