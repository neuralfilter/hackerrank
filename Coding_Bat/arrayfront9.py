def array_front9(nums):
    for i in range(len(nums)):
        if (nums[i] == 9) and (i <= 3):
            return True
    return False
