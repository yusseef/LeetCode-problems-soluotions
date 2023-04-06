class Solution:
    def dfs(self, i: int, j: int, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 0:
            return

        grid[i][j] = 1
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            self.dfs(nx, ny, grid)

    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i*j==0 or i==m-1 or j==n-1) and (grid[i][j]==0):
                    self.dfs(i, j, grid)

        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid)
                    count += 1
        return count