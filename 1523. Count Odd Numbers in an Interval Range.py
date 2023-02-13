class Solution(object):
    def countOdds(self, low, high):
        if low %2 != 0 and high %2 != 0:
            count = (high - low) / 2 + 1
        elif low %2 == 0 and high %2 == 0:
            count = (high - low) / 2 
        else:
            count = ((high - low) / 2) + 1

        return count
        """
        :type low: int
        :type high: int
        :rtype: int
        """