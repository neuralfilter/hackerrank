l = map(int,raw_input().split())
candlehours = l[0]
candlecount = 0
deadcandle = l[0]%l[1]
while(candlecount):
    print candlecount
    print candlehours
    candlehours = (candlehours + ((l[0]- (l[0]%l[1])) / l[1]))
    deadcandle = l[0]%l[1] + deadcandle
    candlecount = (l[0] - (l[0]%l[1])) / l[1]
candlehours = candlehours + ((deadcandle - (deadcandle%l[1]))/l[1]) +candlecount
print candlehours
