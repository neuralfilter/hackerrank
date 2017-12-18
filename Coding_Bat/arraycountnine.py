def array_count9(nums):
    g = 0
    for i in range(len(nums)):
        if nums[i] is 9:
            g+=1
    return g
