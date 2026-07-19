import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for n in nums:
            heapq.heappush(pq, -n)
        
        j = 0
        while j < k:
            j += 1
            res = -heapq.heappop(pq)
            if j == k:
                return res
    