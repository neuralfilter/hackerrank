l = map(int, raw_input().split())
k = map(int, raw_input().split())
counter = 0
for i in range(len(k)):
    if l[0] > k[i]:
        counter+=1
    elif k[i] % l[0] == l[1]:
        counter+=1
    elif i == len(k):
        counter+=1

for f in range(len(k)):
    for h in range(len(k)):
        
