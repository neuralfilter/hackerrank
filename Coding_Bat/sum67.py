def sum67(nums):
    sums = 0
    flag = 0
    for i in range(len(nums)):
        if (nums[i] == 6):
            flag = 1
        if flag == 0:
            sums = sums + nums[i]
        if (nums[i] == 7):
            flag = 0
    return sums
