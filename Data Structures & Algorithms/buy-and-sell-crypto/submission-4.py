class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     # here's the attempted DP solution

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
            
        return maxP
        
        
        
        
'''     
    # this is standard correct sliding window solution
        l = r = maxprofit = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                temp = prices[r] - prices[l]
                maxprofit = max(maxprofit, temp)
                r += 1
            else:
                l, r = r, r + 1
        
        return maxprofit
'''
            
