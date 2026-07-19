import heapq

class KthLargest:

    # idea being we have a max_queue which does sorting
    def __init__(self, k:int, nums:List[int]):
        self.k = k
        self.nums = nums
        maxheap = [-x for x in nums]
        heapq.heapify(maxheap)
        self.pq = maxheap

    def add(self, val:int) -> int:
        self.nums.append(val)
        heapq.heappush(self.pq, -val)

        num = self.k
        storage = []
        while num > 0:
            num -= 1
            temp = heapq.heappop(self.pq)
            storage.append(temp)
            if num == 0:
                for x in storage:
                    heapq.heappush(self.pq, x)
                return -temp
            
            
        



            
        
