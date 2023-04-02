class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[0 : i]) == sum(nums[i +1:]):
                return i
            
        return -1
