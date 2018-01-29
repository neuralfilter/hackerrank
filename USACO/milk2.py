"""
ID: seiji.s1
TASK: milk2
LANG: PYTHON2
"""
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
intervals = []
counter = 0
for i in range(int(fin.readline().rstrip())):
    intervals.append(map(int, fin.readline().rstrip().split()))

intervals.sort()
max_interval = [0, 0]
nomilk_interval = [0]
max_interval[0], max_interval[1] = intervals[0][0], intervals[0][1]

for i in xrange(len(intervals)):
    if (intervals[i][0] <= intervals[i-1][1]) and (intervals[i][1] > intervals[i-1][1]):
        max_interval[1] = intervals[i][1]
        if (intervals[i-1][0] >= intervals[i][0]):
            max_interval[0] = intervals[i][0]
            if (intervals[i][1] >= intervals[i-1][1]):
                max_interval[1] = intervals[i][1]
    if (intervals[i][0] > intervals[i-1][1]):
        nomilk_interval.append(intervals[i][0] - intervals[i-1][1])
fout.write(str(max_interval[1]-max_interval[0]) + " " + str(max(nomilk_interval)) + "\n")
fout.close()
