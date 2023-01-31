class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0]*(1+max(ages))                 
        score_age = sorted(zip(scores, ages))
        
        for score, age in score_age:            
            dp[age] = score + max(dp[:age+1]) 
        return max(dp)                           