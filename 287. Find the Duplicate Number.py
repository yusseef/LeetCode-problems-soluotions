def findDuplicate(nums):
    n = len(nums)
    nums.sort()
    for i in range(0, n):
        if nums[i] == nums[i+1]:
            return nums[i] 

        

