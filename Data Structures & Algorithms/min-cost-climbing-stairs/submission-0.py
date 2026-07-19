class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        j = len(cost) - 1
        while j >= 0:
            if j == len(cost) - 1 or j == len(cost) - 2:
                dp[j] = cost[j]
            else:
                dp[j] = cost[j] + min(dp[j+1], dp[j+2])
            j -= 1
        
        return min(dp[0], dp[1])