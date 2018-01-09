l = map(int, raw_input().split())
bills = [10000, 5000, 1000]
amount_bills = [0,0,0]
while(True):
    
while(True):
    for i in reversed(range(len(bills))):
        while bills[i] < l[1]:
            amount_bills[i] = amount_bills[i] + 1
            l[1] = l[1] - bills[i]
        if bills[i] > l[1]:
           break
        if sum(amount_bills) != l[0]:
            print "-1 -1 -1"
        else:
            print amount_bills[0:2]
print amount_bills

