class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = maxprofit = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                temp = prices[r] - prices[l]
                if temp > maxprofit:
                    maxprofit = temp
                r += 1
            else:
                l, r = r, r + 1
        
        return maxprofit
            
