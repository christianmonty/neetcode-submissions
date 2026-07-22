class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # one way of thinking of this is for each value in 2d array, store in dp the min of 
        # invariant is like if you can move both up and left (backwards), the shorter path is always best beyond that

        # so what do we need to store?
        # dp[0][0] = value in grid
        # if on top row that is dp[0][x] then always is value in grid + dp[left]
        # if in left col that is dp[x][0] then always is value in grid + dp[top]
        # otherwise, dp value is min dp(above) + dp(left)
        # we return last value that is dp[max][max]

        # not sure if we NEED a 2D dp table for this (well an 2d array) or if like coin change, 2d table
        # does 2D DP mean just 2D space required or is it like reframe problem as track 2 separate variables

        # wait do we need to navigate diagonal now? Is that part tricky? How to memoize cleanly

        dp = [[0 for _ in grid[0]] for _ in grid] # form is col inside, row outside


        dp[0][0] = grid[0][0]

        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        # then we want to say i = j = 1. 
        i = 1
        minl = 0
        ncol = len(grid[0])
        nrow = len(grid)
        if ncol < nrow:
            minl = ncol
        else:
            minl = nrow

        while i < minl:
            j = i
            while j < ncol:
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                j += 1
            k = i + 1
            while k < nrow:
                dp[k][i] = grid[k][i] + min(dp[k-1][i], dp[k][i-1])
                k += 1
            
            i += 1

        return dp[len(grid)-1][len(grid[0])-1]
            

            

        
        

        