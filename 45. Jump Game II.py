class Solution(object):
    	def jump(self, nums):
            count = 0
            End = 0
            Farthest = 0
            for i in range(len((nums))-1):
                Farthest = max(Farthest, i + nums[i])
                if i == End:
                    count += 1
                    End = Farthest
    
            return count
        """
        :type nums: List[int]
        :rtype: int
        """