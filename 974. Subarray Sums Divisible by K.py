

def subarraysDivByK(nums, k):
    sublists = [nums[j:i] for i in range(len(nums) +1) for j in range(i)]
    res = [sublist for sublist in sublists if sum(sublist) % k == 0]
    return len(res)








