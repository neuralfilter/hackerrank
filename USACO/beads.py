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
for i in xrange(1, len(beads)/2):
    temp = str(beads[i])
    for x in xrange(len(beads[i:])):
        if (beads[x] == temp) or (beads[x] == "w"):
            length += 1
        else:
            position = x
            break

    temp = str(beads[position])
    for x in xrange(position, len(beads[i:])):
        if (beads[x] == temp) or (beads[x] == "w"):
            length += 1
        else:
            listed.append(length)
            length = 0
            break
if len(listed) == 0:
    fout.write(str(len(beads)/2))
    fout.write("\n")
    fout.close()
    exit()
fout.write(str(max(listed)-1))
fout.write("\n")
fout.close()
