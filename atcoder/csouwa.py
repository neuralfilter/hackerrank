l = map(long, raw_input().split())
nums = map(long, raw_input().split())
sumsarr = []
counter = sum(nums[0:l[1]])
sums = 0
for i in range(0,l[0]-l[1]+1):
    if i == 0:
        sums = sum(nums[0:l[1]])
    else:
        counter = counter - nums[i-1] + nums[i+l[1]-1]
        sums += counter
print sums
