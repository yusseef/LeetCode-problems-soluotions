class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            guess = nums[mid]

            if guess == target:
                return mid

            elif guess > target:
                end = mid - 1
            
            else:
                start = mid + 1

        return -1