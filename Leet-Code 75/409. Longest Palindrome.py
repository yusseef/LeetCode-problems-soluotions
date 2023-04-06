class Solution:
    def longestPalindrome(self, s: str) -> int:
        singles = set()
        length = 0

        for char in s:
            if char in singles:
                singles.remove(char)
                length += 2
            else:
                singles.add(char)
        
        if len(singles) > 0:
            length += 1
        
        return length
