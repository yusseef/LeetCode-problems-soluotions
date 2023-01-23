class Solution(object):
    def twoSum(self, nums, target):
        values = dict()
        for i, elem in enumerate(nums):
            x = target - elem
            if x in values:
                return [values[x], i]
            values[elem] = i
    
        return []
        