class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        hmc = set()
        totalarea = 0
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def isValid(row: int, col: int):
            if row < 0 or row > rows or col < 0 or col > cols:
                return False
            if grid[row][col] == 0 or (row, col) in hmc:
                return False
            return True

        def recurse(row: int, col: int) -> int:
            hmc.add((row, col))
            retarea = 1            
            for d in directions:
                a = row + d[0]
                b = col + d[1]
                if isValid(a, b):
                    retarea += recurse(a, b)
            return retarea

        for i in range(0, rows + 1):
            for j in range(0, cols + 1):
                if isValid(i, j):
                    retval = recurse(i, j)
                    if retval > totalarea:
                        totalarea = retval

        return totalarea