l = map(int, raw_input().split())
paths = [0,0,0,0]
paths[0] = (l[0] + l[1]) * 2
paths[1] = (l[0] + l[1] + l[2])
paths[2] = (l[1] + l[2]) * 2
paths[3] = (l[2] + l[0]) * 2
print min(paths)
