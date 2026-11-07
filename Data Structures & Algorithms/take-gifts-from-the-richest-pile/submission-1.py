import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        pq = []
        for g in gifts:
            heapq.heappush(pq, -g)

        j = 0
        while j < k:
            tmp = -heapq.heappop(pq)
            nxt = math.floor(math.sqrt(tmp))
            heapq.heappush(pq, -nxt)
            j += 1

        
        return -sum(pq)
        