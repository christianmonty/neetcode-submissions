class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        r = len(prices) - 1
        dp = [0] * len(prices)

        for i in range(len(prices) - 1, -1, -1):
            maxp = 0

            for j in range(i+1, len(prices)):
                maxp = max(maxp, dp[j] + prices[j] - prices[i], dp[j])
            dp[i] = maxp
        
        return dp[0]
                
