class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def isValid(row: int, col: int) -> bool:
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            return True


        def fanout(r: int, c: int):
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return
    
            for d in dir:
                r2 = r + d[0]
                c2 = c + d[1]
                if isValid(r2, c2):
                    fanout(r2, c2)

        count = 0
        for idx1, row in enumerate(grid):
            for idx2, col in enumerate(grid[idx1]):
                if grid[idx1][idx2] == '1':
                    fanout(idx1, idx2)
                    count += 1
        
        return count