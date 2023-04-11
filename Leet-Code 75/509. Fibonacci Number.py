class Solution:
    def fib(self, n: int) -> int:
        def fibnum(x,dic1):
            if x in [0,1]:
                return x
            elif x not in dic1:
                dic1[x]=fibnum(x-1,dic1)+fibnum(x-2,dic1)
            return dic1[x]
        mydict={}
        return fibnum(n,mydict)
        
       