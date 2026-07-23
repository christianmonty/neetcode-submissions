class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # invariant is if both left and up are available, increase path count by 2, else
        # if first and last are not 0, there is no path. If they are, there MAY be a path
        # can there be odd # of paths? Yes if only a single path
        # so look above or left. If one exists, make it's path # equal to yours. 
        # then at the top left, sum up both to right and below

        # then start at bottom (or top). 
        # first populate DP array to have 0 where all the 1's are or we do this implicitly below
        # if obstacleGrid == 1, then we skip that dp since can't propagate anything!

        dp = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]

        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
            return 0

        dp[0][0] = 1

        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break

        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        

        i = 1
        minsiz = 0
        if len(obstacleGrid) < len(obstacleGrid[0]):
            minsiz = len(obstacleGrid)
        else:
            minsiz = len(obstacleGrid[0])


        while i < minsiz:
            j = i
            while j < len(obstacleGrid):
                if obstacleGrid[j][i] == 0:
                    dp[j][i] = dp[j-1][i] + dp[j][i-1]
                j += 1
            k = i + 1
            while k < len(obstacleGrid[0]):
                if obstacleGrid[i][k] == 0:
                    dp[i][k] = dp[i-1][k] + dp[i][k-1]
                k += 1

            i += 1

        return dp[len(dp)-1][len(dp[0])-1]



