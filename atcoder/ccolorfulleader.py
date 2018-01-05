ignore = input()
l = map(int, raw_input().split())
temp = []
counter = 0
if ignore == 1:
    print 1, 1
    exit()
for i in range(len(l)):
    if (1 <= l[i] <= 399) and ("Grey" not in temp):
        temp.append("Grey")
    elif (400 <= l[i] <= 799) and ("Brown" not in temp):
        temp.append("Brown")
    elif (800 <= l[i] <= 1199) and ("Green" not in temp):
        temp.append("Green")
    elif (1200 <= l[i] <= 1599) and ("Water" not in temp):
        temp.append("Water")
    elif (1600 <= l[i] <= 1999) and ("Blue" not in temp):
        temp.append("Blue")
    elif (2000 <= l[i] <= 2399) and ("Yellow" not in temp):
        temp.append("Yellow")
    elif (2400 <= l[i] <= 2799) and ("Turq" not in temp):
        temp.append("Turq")
    elif (2800 <= l[i] <= 3199) and ("Red" not in temp):
        temp.append("Red")
    elif (l[i] >= 3200):
        counter+=1
if counter == 0:
    print len(temp), len(temp)
elif len(temp) == 0:
    print 1 , (len(temp) + counter)
else:
    print len(temp), (len(temp) + counter)
