l = map(int,raw_input().split())
k = map(int, raw_input().split())
item_number = 0
k.sort()
itemcost = k[0:(l[1])]
for i in range(l[1]):
    itemcost[i] = itemcost[i] + i

print sum(itemcost)
