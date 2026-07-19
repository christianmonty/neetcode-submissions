import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #trick with these backtracking problems 
        l, r = 1, max(piles)
        k = r

        def rate(low: int, high: int) -> int:
            while low <= high:
                mid = (low+high)//2
                if testMid(mid):
                    k = mid
                    high = mid-1
                else:
                    low = mid+1
            return k

        def testMid(mid: int) -> bool:
            sumh = 0
            for val in piles:
                sumh += math.ceil(val/mid) #linear
                if sumh > h:
                    return False
            return True

        return rate(l, r)