from collections import Counter

ignore = int(raw_input())
shoesize = Counter(map(int, raw_input().split()))
customer = int(raw_input())

earnings = 0

desired = [map(int, raw_input().split()) for x in range(customer)]
for i in range(len(desired)):
    if shoesize[int(desired[i][0])] > 0:
        earnings += desired[i][1]
        shoesize[int(desired[i][0])] -= 1

print earnings
