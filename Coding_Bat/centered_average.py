def centered_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))
    sums = 0
    for i in range(len(nums)):
       sums = sums + nums[i]
    return (sums) / len(nums)
