from itertools import permutations

string = map(str, raw_input().split())

perms = list(permutations(string[0], int(string[1])))
#perms = perms.sort(key = lambda a:a[0])

for i in range(len(perms)):
    print "".join(perms[i])
