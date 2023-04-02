nums = [1,2,3,4]
res = [sum(nums[0:i + 1]) for i in range(len(nums))]

    
print(res)