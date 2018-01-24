"""
ID: seiji.s1
TASK: friday
LANG: PYTHON2
"""
weekday = 0
counter = [0]*7
fin = open("friday.in", "r")
fout = open("friday.out", "w")
for i in xrange(int(fin.readline())):
    year = 1900 + i
    for cur_month in xrange(1, 13):
        if cur_month in [4, 6, 9, 11]:
            days = 30
        elif cur_month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31
        elif cur_month == 2:
            if ((year % 4 == 0) and (year % 100 > 0)) or ((cur_month == 2) and (year % 400 == 0)):
                days = 29
            else:
                days = 28
        for x in xrange(1, days+1):
            if x == 13:
                counter[weekday] += 1
            if weekday == 6:
                weekday = 0
            else:
                weekday += 1
fout.write(" ".join(map(str, counter[5:7])))
fout.write(" ")
fout.write(" ".join(map(str, counter[0:5])))
fout.write("\n")
fout.close()
