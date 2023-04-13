class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output,left,dic=0,0,{}
        for right in range(len(s)):
            dic[s[right]]=1+dic.get(s[right],0)
            while (right-left+1)-max(dic.values())>k:
                dic[s[left]]-=1
                left+=1
            output=max(output,right-left+1)
        return output