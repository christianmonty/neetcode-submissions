import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxq = []
        for s in stones:
            heapq.heappush(maxq, -s)
        
        while maxq:
            if len(maxq) == 1:
                return -heapq.heappop(maxq)
            num1 = -heapq.heappop(maxq)
            num2 = -heapq.heappop(maxq)
            res = abs(num1 - num2)
            heapq.heappush(maxq, -res)
        