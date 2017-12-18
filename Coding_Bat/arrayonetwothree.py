def array123(nums):
    ott = [1,2,3]
    if ott == nums:
        return True
    for i in range(len(nums)-2):
        print nums[i:i+3]
        if (nums[i:i+3] == ott):
            return True
    return False
