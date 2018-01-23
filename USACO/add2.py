"""
ID:seiji.s1
LANG: PYTHON2
TASK: test
"""

fin = open('test.in', "r")
fout  = open('test.out', "w")

x, y = map(int, fin.readline().split())
summ = x+y
fout.write(str(summ) + "\n")
fout.close()
