"""
ID:
"""

fin = open('test.in', "r")
fout  = open('test.out', "w")

x, y = map(int, fin.readline().split())
print x+y
fout.close()
