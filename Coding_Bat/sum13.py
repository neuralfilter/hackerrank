def sum13(nums):
    totals = 0
    if(nums):
        for i in range(len(nums)):
            if ((nums[i] != 13) and (nums[i-1] != 13)) or ((i == 0) and
                                                           (nums[i] != 13)):
                print nums[i]
                totals+=nums[i]
        return totals
    else:
        return 0
