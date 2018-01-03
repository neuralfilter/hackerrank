l = map(int, raw_input().split())
if l[0] < l[1]:
    print ((l[2]  - (l[2] % l[0]))/ (l[0]))
elif (l[0] > l[1]) or (l[0] == l[1]):
    print ((l[2] - (l[2] % l[1]))/ (l[1]))
