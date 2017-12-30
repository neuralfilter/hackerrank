l = int(raw_input())
k = list(raw_input())
counter = [0,0]
for i in range(len(k)):
    if k[i] == "A":
        counter[0] = counter[0] + 1
    if k[i] == "D":
        counter[1] = counter[1] + 1
if counter[0] > counter[1]:
    print "Anton"
elif counter[0] < counter[1]:
    print "Danik"
elif counter[0] == counter[1]:
    print "Friendship"
