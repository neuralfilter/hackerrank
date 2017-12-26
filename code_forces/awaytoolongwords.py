N = input()
a = [raw_input() for i in range(N)]
for i in range(len(a)):
    if len(a[i]) <= 10:
        print a[i]
    else:
        print a[i][0] + str(len(a[i])-2) + a[i][len(a[i])-1]
