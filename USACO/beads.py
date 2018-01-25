"""
ID: seiji.s1
TASK: beads
LANG: PYTHON2
"""
fin = open("beads.in", "r")
fout = open("beads.out", "w")
fin.readline()
beads = list(fin.readline().rstrip())*2
listed = []
counter = 0
position = 0
length = 0
for i in xrange(1, len(beads)):
    temp = beads[i]
    for x in xrange(len(beads[i:])):
        if (beads[x] == temp) or (beads[x] == "w"):
            length += 1
    counter += 1

fout.write("\n")
fout.close()
