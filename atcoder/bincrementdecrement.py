inputted = int(raw_input())
l = list(raw_input())
x = 0
record = []
record.append(x)
for i in range(len(l)):
    if l[i] == "I":
        x+=1

    elif l[i] == "D":
        x-=1
    record.append(x)
print max(record)
