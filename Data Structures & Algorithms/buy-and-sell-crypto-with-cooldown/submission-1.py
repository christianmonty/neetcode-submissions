class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        size = len(prices)
        best = [0] * size
        best[size-1] = 0

        if size > 1:
            best[size-2] = max(best[size-1], prices[size-1] - prices[size-2])

        for i in range(size - 3, -1, -1):
            tempbest = 0
            j = i + 1

            while j < size:
                tempbest = max(tempbest, best[j], prices[j] - prices[i] + (best[j+2] if j + 2 < size else 0))
                j += 1
            best[i] = tempbest


        return best[0]
        
        
        
        
        
        
        
        
        
        
        # for each sell, need to check: buy, sell on next day and take dp of following day
        # compared to not?
        # so would see maxProfit[0][1] + [2][4] = 6, which is max. Of that + maxProfit[0][1] + bestArr[2], update bestArr[0]
        # then take max over that linear array
        # what about multiple times? Well if start from back, then maybe replace best from in bestarr (backwards to forwards)
        # or more simply iterate backwards & best array, can try buy 3, sell at 4 and take following profit
        # then find buy 1, sell at 4 and take following profit. Or buy 1, sell at 3 and take 4's profit or next best (tricky?)
        # wait missing cooldown period of 1 day, so that complicates things!
        # what if try (take ours and sell on best day and take following after, OR skip current and buy next)
        # [                   4 4 4 0]

        """                 Day sold
        Day bought  0 1 2 3 4 5 6 7....
        0           0 2 3 -1 3
        1             0 1 -3 1
        2               0 -4 0
        3                  0 4
        4
        5
        6
        7
        """

        