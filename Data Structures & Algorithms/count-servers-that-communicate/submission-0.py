class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        # dfs way to do this is expand four directions until find another 1 or at edge
        # the greedy part is stop as soon as you find one

        # another idea is store in hashmap for each row, and also each column if count > 1. If 2, iteratively go through all cells in grid and check if either it's row > 2 or col > 2 and count it if it is
        # we only have to note communicating with ANY other server, not how many they communicate with

        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i: int, j: int, d: int) -> bool:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            res = dfs(i + dir[d][0], j + dir[d][1], d)
            if res:
                return True
            return False
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for index, val in enumerate(dir):
                        l = val[0]
                        u = val[1]
                        if dfs(i + l, j + u, index):
                            count += 1
                            break
        return count