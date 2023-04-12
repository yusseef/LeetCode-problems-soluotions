class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[0 for _ in range(n+1)] for _ in range(m+1)]
        def db(x,y):
            if x==m and y==n:
                return 1
            elif x==m:
                if memo[x][y+1]==0:
                    memo[x][y+1]=db(x,y+1)
                return memo[x][y+1]
            elif y==n:
                if memo[x+1][y]==0:
                    memo[x+1][y]=db(x+1,y)
                return memo[x+1][y]
            else:
                if memo[x][y+1]==0:
                    memo[x][y+1]=db(x,y+1)
                if memo[x+1][y]==0:
                    memo[x+1][y]=db(x+1,y)
                return memo[x][y+1]+memo[x+1][y]
        return db(1,1)