class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        X = nums[:n]
        Y = nums[n:]
        res = []
        for i in range(n):
            res.append(X[i])
            res.append(Y[i])
        
        return res