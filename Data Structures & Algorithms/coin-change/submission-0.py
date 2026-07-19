class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        if amount <= 0:
            return 0
            
        for c in coins:
            if c <= amount:
                dp[c] = 1

        for i in range(amount + 1):
            minnum = dp[i]
            for c in coins:
                if (i - c) >= 0:
                    temp = 1 + dp[i-c]
                    if temp < minnum:
                        minnum = temp

            dp[i] = minnum
        
        return dp[amount] if dp[amount] < float('inf') else -1

