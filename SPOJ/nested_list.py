lowest = 0
second_lowest = 0
names = []
array_size = int(raw_input())
nested_list = [[]]*array_size

for i in range(array_size):
    name = raw_input()
    score = float(raw_input())
    nested_list[i] = [name, score]

nested_list.sort(key=lambda sublist: sublist[1])

for s in range(i):
    if(nested_list[1][1] == nested_list[s][1]):
        names.append(nested_list[s][0])

names.sort()

for g in range(len(names)):
    print(names[g])
