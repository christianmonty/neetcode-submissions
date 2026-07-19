class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we need to update values in place

        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        directions = [[-1, 0], [0, -1], [1,0], [0,1]]

        def percolate(row: int, col: int):
            q = []
            q.append((row, col))

            while q:
                res = q.pop(0)
                resr = res[0]
                resc = res[1]
                oldres = grid[resr][resc]

                for d in directions:
                    a = resr + d[0]
                    b = resc + d[1]
                    if a >= 0 and a <= rows and b >= 0 and b <= cols:
                        if oldres + 1 < grid[a][b]:
                            grid[a][b] = oldres + 1
                            q.append((a, b))

        for i in range(0, rows+1):
            for j in range(0, cols+1):
                if grid[i][j] == 0:
                    percolate(i, j)