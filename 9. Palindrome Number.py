class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        
        rev = str(x)[::-1]

        return True if rev == str(x) else False