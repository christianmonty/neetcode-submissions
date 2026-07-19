import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        outlist = []
        hq = []

        for item in points:
            dist = math.sqrt((item[0]**2)+(item[1]**2))
            heapq.heappush(hq, (dist, item[0], item[1]))
        
        j = 0
        while j < k:
            res = heapq.heappop(hq)
            reslist = [res[1], res[2]]
            outlist.append(reslist)
            j += 1
        return outlist