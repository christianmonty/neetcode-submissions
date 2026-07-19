import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        newlist = []
        heapq.heapify(newlist)

        for i in nums:
            if len(newlist) < k:
                heapq.heappush(newlist, i)
            else:
                if i > newlist[0]:
                    heapq.heappop(newlist)
                    heapq.heappush(newlist, i)

        return heapq.heappop(newlist)












        '''
        # below max heap works but is not nlogk efficient it's nlogn
        newlist = [-x for x in nums]
        heapq.heapify(newlist)

        for i in range(1, k):
            heapq.heappop(newlist)

        return -heapq.heappop(newlist)
        '''

