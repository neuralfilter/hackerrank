l = map(int, raw_input().split())
points = map(int, raw_input().split())
cor = 0
for i in range(1,len(points)):
    if ((points[i]-points[i-1])*l[1]) > l[2]:
        cor+=l[2]
    elif ( (points[i]-points[i-1])*l[1])< l[2]:
        cor+=(points[i]-points[i-1])*l[1]

print cor
