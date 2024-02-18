from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    # count islands starting here
                    num_islands += 1
                    self.countIslands(r, c, grid)
        return num_islands

    
    def countIslands(self, r, c, grid):
        if r >= len(grid) or c >= len(grid[0]) or c < 0 or r < 0:
            return
        if grid[r][c] == "0":
            return
        
        if grid[r][c] == "1":
            grid[r][c] = "0"
            # left
            self.countIslands(r, c-1, grid)
            # down
            self.countIslands(r+1, c, grid)
            # right
            self.countIslands(r, c+1, grid)
            # top
            self.countIslands(r-1, c, grid)
