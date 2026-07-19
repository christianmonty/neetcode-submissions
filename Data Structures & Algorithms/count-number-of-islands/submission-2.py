class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(r: int, c: int) -> bool:
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False
            return True

        def countIslands(r: int, c: int):
            grid[r][c] = '0'
            for d in directions:
                row = r + d[0]
                col = c + d[1]
                if isValid(row, col) and grid[row][col] == '1':
                    countIslands(row, col)


        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    countIslands(i, j)
                    count += 1

        return count