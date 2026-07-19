class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def fanout(r: int, c: int):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            fanout(r-1, c)
            fanout(r+1, c)
            fanout(r, c-1)
            fanout(r, c+1)
            return
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    fanout(i, j)
                    islands += 1
        
        return islands


        