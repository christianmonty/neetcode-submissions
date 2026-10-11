class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def isValid(i: int, j: int) -> bool:
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return False
            return True

        # function takes input of specific coordinates, calculates len longest increasing path
        def recurse(i: int, j: int) -> int:
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            maxpath = 0
            for r, c in dir:
                nr = i + r
                nc = j + c
                if isValid(nr, nc) and matrix[nr][nc] > matrix[i][j]:
                    temp = recurse(nr, nc)
                    maxpath = max(maxpath, temp)

            dp[(i, j)] = 1 + maxpath
            return 1 + maxpath
        
        totalmax = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = recurse(i, j)
                totalmax = max(totalmax, res)
        return totalmax
            
        