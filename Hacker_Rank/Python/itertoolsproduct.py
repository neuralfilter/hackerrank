from itertools import product
k = map(int, raw_input().split())
l = map(int, raw_input().split())

print(" ".join(map(str, product(k,l))))
