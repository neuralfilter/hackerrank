arr = []

for i in range(int(raw_input())):
    temp = map(int, raw_input().split())
    if abs(temp[2] - temp[0]) < abs(temp[2] - temp[1]):
        print "Cat A"
    elif abs(temp[2] - temp[0]) > abs(temp[2] - temp[1]):
        print "Cat B"
    elif abs(temp[2] - temp[0]) == abs(temp[2] - temp[1]):
        print "Mouse C"
