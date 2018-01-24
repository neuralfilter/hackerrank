"""
ID: seiji.s1
TASK: gift1
LANG: PYTHON2
"""
from collections import OrderedDict
fin = open("gift1.in", "r")
fout = open("gift1.out", "w")

names = OrderedDict(tuple(((fin.readline().strip()), 0) for i in range(int(fin.readline().strip()))))

while True:
    person = fin.readline().strip()
    if len(person) == 0:
        break
    val, div = map(int, fin.readline().strip().split())
    names[person] -= val
    if div != 0 and val % div > 0:
        names[person] += (val % div)
    for i in range(div):
        if (val % div > 0):
            names[fin.readline().strip()] += (val - (val % div)) / div
        elif (val % div == 0):
            names[fin.readline().strip()] += val / div
        else:
            names[fin.readline().strip()] += 0

for key, value in names.items():
    fout.write(key + " " + str(value) + "\n")
fout.close()
