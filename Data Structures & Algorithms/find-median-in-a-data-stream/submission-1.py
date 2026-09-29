import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # hold smaller half
        self.large = [] # hold larger half
        

    def addNum(self, num: int) -> None:
        # thinking through cases, if even #, next one either add to small if smaller or equal than large #, or switch out large[0] if larger than that
        # if odd #, next one either if < small[0] then pop out small[0] add to large, else just add to large
        if (len(self.small) + len(self.large)) % 2 == 0:
            if self.large and num > self.large[0]:
                heapq.heappush(self.small, -heapq.heappop(self.large))
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -num)
        else:
            if num < -self.small[0]:
                heapq.heappush(self.large, -heapq.heappop(self.small))
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)

        

    def findMedian(self) -> float:

        # if total is odd, return largest of small
        # if total is even, return average of both
        if len(self.small) > len(self.large):
            return -self.small[0] # top of heap
        else:
            return (-self.small[0] + self.large[0]) / 2
        
        

    # okay so brute force, addNum adds to end of list
    # since have length of list, return middle element
    # if even nonzero length, return average of middle two
    # tradeoff here is need 50k sized aray
    # wait we assumed the list would be sorted, which it is apparently not
    # so brute force would be sorting EVERY TIME findMedian is called, not ideal...

    # instead I figured 2 priority queues is optimal solution for leetcode hard
    # from peeking at solution ideas, one as smallest (neg pq) one as largest, take [0] of each