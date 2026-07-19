class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * n

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = 1
            elif i == n-2:
                dp[i] = 2
            else:
                dp[i] = dp[i+1] + dp[i+2]


        return dp[0]
            