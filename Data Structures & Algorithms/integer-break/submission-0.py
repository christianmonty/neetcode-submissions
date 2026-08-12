class Solution:
    def integerBreak(self, n: int) -> int:

        # every number that evenly divides n will be summed can be multiplied into a product
        # so from n = 1 to n // 2
        # if n % i == 0, then try doing i ** (n // i) to see how high
        # where is the DP storage savings?
        # well 12 max is 6 max * 6 max, do dp[6] * the leftover
        # dp[1] = 1. dp[2] = 1 (1 + 1 = 2)
        # dp[3] = 2 + 1?

        # wait I missed that doesn't have to be same integer k times
        # it can be ANY integers summed up to n
        # so outer loop i is 3 to n, have 2
        # inner loop j is 1 to i
        # referenced a solution to understand what problem is asking

        dp = [1] * (n+1)
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i): # thinking being j is smaller always
                dp[i] = max(dp[i], j * dp[i-j], (i-j) * j)

        return dp[n]

