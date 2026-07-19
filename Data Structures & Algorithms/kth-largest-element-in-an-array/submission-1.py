import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        newlist = [-x for x in nums]
        heapq.heapify(newlist)

        for i in range(1, k):
            heapq.heappop(newlist)

        return -heapq.heappop(newlist)

