"""
ID: seiji.s1
TASK: milk2
LANG: PYTHON2
"""
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
arr = [0, 0]
previnterv = [0, 0]
nomilk = 0
for i in range(int(fin.readline().rstrip())):
    intervals = map(int, fin.readline().rstrip().split())
    if i == 0:
        arr[0] = intervals[0]
    if (intervals[0] <= arr[0]) and (intervals[1] >= arr[0]):
        nomilk = 0
        arr[0], arr[1] = intervals[0], intervals[1]
    if (intervals[0] <= arr[1]):
        arr[1] = intervals[1]
    if intervals[0] > previnterv[1]:
        nomilk = intervals[0] - previnterv[1]
    previnterv[0], previnterv[1] = intervals[0], intervals[1]
    print arr
fout.write(str(arr[1]-arr[0]) + " " + str(nomilk) + "\n")
fout.close()
