class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        self.nrow = len(board)

        goal = self.nrow * self.nrow
        
        queue = [(1, 0)]
   
        visited = set()
        
        while queue:
            cur, step = queue.pop(0)
            if cur == goal:
                return step
            
            for move in range(1, 7):
                ncell = cur + move
                if ncell > goal:
                    break
                r, c = self.n2rc(ncell)
                if (r, c) not in visited:
                    visited.add((r, c))
                    if board[r][c] != -1:
                        ncell = board[r][c]
                    queue.append((ncell, step + 1))
        
        return -1
                        
                        
    def n2rc(self, n):        
        row = (n - 1) // self.nrow
        row = self.nrow - row - 1
        
        col = (n - 1) % self.nrow
        if (self.nrow - row) % 2 == 0:
            col = self.nrow - col - 1
        return row, col