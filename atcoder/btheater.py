first = int(raw_input())
k = [map(int, raw_input().split()) for i in range(first)]
audience = 0
for i in range(len(k)):
    audience = audience + k[i][1] - k[i][0] + 1

print audience
