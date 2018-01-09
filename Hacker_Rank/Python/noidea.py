ignore = map(int, raw_input().split())
l = (map(int, raw_input().split()))
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))
happi = 0
for i in l:
    if i in a:
        happi+=1
    elif i in b:
        happi-=1

print happi
