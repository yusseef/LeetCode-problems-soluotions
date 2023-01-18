class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        Sum = sum(nums)
        res = nums[0]
        maxSub = nums[0]
        minSub = 0
        for i in range(1,len(nums)):
            maxSub = max(maxSub+nums[i], nums[i])
            minSub = min(minSub+nums[i], nums[i])
            res = max(res, maxSub, Sum - minSub)
        return res