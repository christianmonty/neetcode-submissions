import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        outlist = [-float("inf") for _ in range(len(nums) - k + 1)]
        
        front = i = 0
        end = k - 1

        # wait issue is set shows membership, bin heap shows max in subset
        # but we have to keep order in mind, and also max
        # we could just have maxheap, and store index.
        # if we throw away max, keep popping while index invalid...
        kmax = nums[0]
        pq = []

        while i <= end:
            kmax = max(kmax, nums[i])
            heapq.heappush(pq, (-nums[i], i))
            i += 1

        f = 0
        e = end
        while f < len(outlist):
            # invariant here is that pq holds all items
            outlist[f] = -pq[0][0]
            
            # pop from pq, if max is being used or is dated
            while pq and pq[0][1] <= f:
                heapq.heappop(pq)

            f += 1
            e += 1
            if e < len(nums):
                heapq.heappush(pq, (-nums[e], e))

        return outlist


