arr = []
for i in range(int(raw_input())):
    value = int(raw_input())
    print len([i for i in map(int, list(str(value))) if i != 0 and value % i == 0])
