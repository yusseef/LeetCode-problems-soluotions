class Solution(object):
    def zeroFilledSubarray(self, nums):
        n = len(nums)
        ans = 0
        count = 0 
        for i in range(n):
            if nums[i] == 0:
                count += 1
                ans += counter
            else:
                count = 0 
        return ans

