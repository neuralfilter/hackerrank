num_par, low_bound = map(int, raw_input().split())
scores = (map(int, raw_input().split())) 
boundary = scores[low_bound-1]
counter = 0
for s in range(len(scores)):
    if (scores[s] < boundary) or (scores[s] == 0):
        counter+=1
print len(scores)-counter
