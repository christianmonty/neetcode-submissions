class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # this is the same as largest island, turns blocks into 0 maybe or -1?
        # store a maxCount
        # maybe we used visited set for a BFS connected component
        # or we used DFS and turn values into 0, adding cell value to total. Return cell value


        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            subtotal = grid[i][j]
            grid[i][j] = 0
            ddir = [[0, 1], [1,0], [-1, 0], [0,-1]]

            for r, c in ddir:
                nr = i + r
                nc = j + c
                subtotal += dfs(nr, nc)
            return subtotal

        tmax = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmax = max(tmax, dfs(i, j))
        return tmax
