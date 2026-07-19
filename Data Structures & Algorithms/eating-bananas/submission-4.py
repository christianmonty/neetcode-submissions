import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checkCount(k: int) -> bool:
            sum = 0
            for p in piles:
                sum += math.ceil(p / k)
            if sum > h:
                return False
            return True

        high = max(piles)
        best = high

        l, r = 1, high
        
        while l <= r:
            mid = (l + r) // 2
            if checkCount(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return best

