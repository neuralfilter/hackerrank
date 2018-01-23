"""
ID: seiji.s1
TASK: ride
LANG: PYTHON2
"""
fin = open('ride.in', "r")
fout = open('ride.out', "w")

k = (fin.readline().rstrip())
j = (fin.readline().rstrip())
m = [ord(k[i])-64 for i in range(len(k))]
n = [ord(j[f])-64 for f in range(len(j))]
#print m, n
if  (reduce(lambda x, y: x*y, m) % 47) == (reduce(lambda x, y:x*y, n) % 47):
    fout.write("GO" + "\n")
else:
    fout.write("STAY" + "\n")

fout.close()
