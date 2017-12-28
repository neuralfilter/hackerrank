l = int(raw_input())
tsteps = l
counter = 0
for i in reversed(range(1,6)):
    while(i <= tsteps):
        tsteps = tsteps - i
        counter+=1
print counter
