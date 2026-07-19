import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x, y):
            return math.sqrt(x**2 +y**2)

        pq = []
        heapq.heapify(pq)

        # this is tuple unpacking, vs. enumerate is index, value
        for x, y in points:
            dist = distance(x, y)

            if len(pq) < k:
                heapq.heappush(pq, (-dist, x, y))
            elif -dist > pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, (-dist, x, y))

        outlist = []
        while pq:
            item = heapq.heappop(pq)
            newlist = [item[1], item[2]]
            outlist.append(newlist)

        return outlist

