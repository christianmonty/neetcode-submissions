import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #trick with these backtracking problems 
        maxb = 0
        sumb = 0
        for val in piles:
            sumb += val
            if val > maxb:
                maxb = val
        
        def rate(low: int, high: int) -> int:
            k = maxb
            while low <= high:
                mid = (low+high)//2
                res = testMid(mid)
                if res:
                    k = mid
                    high = mid-1
                else:
                    low = mid+1
            return k

        def testMid(mid: int) -> bool:
            i, j = 0, 0
            sumh = 0
            if mid < sumb/h:
                return False
            while i < len(piles):
                sumh += math.ceil(piles[i]/mid) #linear
                if sumh > h:
                    return False
                i += 1
            return True

        return rate(0, maxb)