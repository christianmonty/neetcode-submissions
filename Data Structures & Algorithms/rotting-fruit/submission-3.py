class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        directions = [[-1, 0], [0, -1], [1,0], [0,1]]
        indices = []
        freshcount = 0
        for i in range(0, rows+1):
            for j in range(0, cols+1):
                if grid[i][j] == 2:
                    indices.append([i, j])
                elif grid[i][j] == 1:
                    freshcount += 1
        if not freshcount:
            return 0

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
                        if grid[a][b] == 1 or oldres + 1 < grid[a][b]:
                            grid[a][b] = oldres + 1
                            if (a,b) not in q:
                                q.append((a, b))
                            

        for thing in indices:
            percolate(thing[0], thing[1])

        maxcount, numtwos = 0, 0
        for i in range(0, rows+1):
            for j in range(0, cols+1):
                if grid[i][j] == 1:
                    return -1
                if grid[i][j] > maxcount:
                    maxcount = grid[i][j]
                if grid[i][j] == 2:
                    numtwos += 1
        
        if maxcount != 2 or numtwos >= len(indices):
            return maxcount - 2
        return -1
