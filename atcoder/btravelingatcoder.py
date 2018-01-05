ignore = input()
l = map(int, raw_input().split())
l.sort()
counter = 0
for i in range(1,len(l)):
    counter = counter + l[i]-l[i-1]

print counter
