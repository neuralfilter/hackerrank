k = list(raw_input())
time = "".join(k[0:len(k)-2])
time = map(int, time.split(":"))
ampm = "".join(k[len(k)-2:len(k)])


if ((ampm == "AM") and (time[0] < 12)) or ((ampm == "PM") and (time[0] > 12)):
    if (len(str(time[0])) != 2):
        time[0] = "0" + str(time[0])
    if (len(str(time[1])) != 2):
        time[1] = "0" + str(time[1])
    if (len(str(time[2])) != 2):
        time[2] = "0" + str(time[2])
    print ":".join(map(str, time))
elif (ampm == "PM") and (time[0] < 12):
    time[0] = time[0] + 12
    if (len(str(time[1])) != 2):
        time[1] = "0" + str(time[1])
    if (len(str(time[2])) != 2):
        time[2] = "0" + str(time[2])
    print ":".join(map(str, time))
elif (ampm == "AM") and (time[0] >= 12):
    time[0] = time[0] - 12
    if (len(str(time[0])) != 2):
        time[0] = "0" + str(time[0])
    if (len(str(time[1])) != 2):
        time[1] = "0" + str(time[1])
    if (len(str(time[2])) != 2):
        time[2] = "0" + str(time[2])
    print ":".join(map(str, time))
else:
    print ":".join(map(str, time))
