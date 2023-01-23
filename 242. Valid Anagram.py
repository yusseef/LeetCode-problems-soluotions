class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s = list(s)
        lst_t = list(t)
        lst_s.sort()
        lst_t.sort()
        if lst_s == lst_t:
            return True
        return False
        