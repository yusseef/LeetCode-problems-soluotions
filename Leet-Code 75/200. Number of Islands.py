class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island=0
        
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_island += 1
                    dfs(i,j)
                    
        return num_island
