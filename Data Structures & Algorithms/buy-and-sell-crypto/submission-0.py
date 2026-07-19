class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        best = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            best = max(best, prices[r] - prices[l])
            r += 1
        return best