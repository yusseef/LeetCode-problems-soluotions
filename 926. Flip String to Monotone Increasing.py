class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        ones, ans = 0, 0                    
                                            
        for num in s:                                                       
            if num =='1': ones += 1         
            elif ones:                      
                ones -= 1                   
                ans += 1                    
        return ans