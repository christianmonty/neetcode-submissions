import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.largest = k
        for n in nums:
            heapq.heappush(self.pq, -n)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)

        j = 0
        templist = []
        while j < self.largest:
            j += 1
            res = -heapq.heappop(self.pq)
            templist.append(res)
            if j == self.largest:
                for val in templist:
                    heapq.heappush(self.pq, -val)
                return res
            
        
