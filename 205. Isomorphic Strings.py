class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        
        if len(s)==0 or len(t)==0:
            return False
        
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dict.values():  
                    return False
                dict[s[i]] = t[i]
        return True
