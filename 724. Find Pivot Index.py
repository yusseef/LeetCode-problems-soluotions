class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        TotalSum = sum(nums)
        right = TotalSum
        left = 0
        for i in range(len(nums)):
            Current = nums[i]

            right -= Current

            if right == left:
                return i
            
            left += Current
        
        return -1