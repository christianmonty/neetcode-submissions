class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # need to continually combine the two smallest and add it back to pq
        # sum of two smallest gets added to the cost

        heapq.heapify(sticks)
        total = 0

        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            sec = heapq.heappop(sticks)
            ssum = first + sec
            total += ssum
            heapq.heappush(sticks, ssum)
        
        return total

