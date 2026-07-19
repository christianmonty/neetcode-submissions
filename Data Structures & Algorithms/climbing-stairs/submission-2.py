class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        dp[n-1] = 1
        if n > 1:
            dp[n-2] = 2
        j = n-3
        while j >= 0:
            dp[j] = dp[j+1] + dp[j+2]
            j -= 1


        return dp[0]