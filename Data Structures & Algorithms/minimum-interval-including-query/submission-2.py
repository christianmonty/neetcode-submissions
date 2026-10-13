import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # now implementing one of the solutions (Min Heap)
        # process queries in sorted order, add intervals whose start <= q
        # among active intervals remove any that end before q
        # smallest valid interval is always at top of min heap (ordered by interval length)

        intervals.sort()
        newq = sorted(queries)
        i = 0
        minHeap = [] # (interval length, interval end)
        res = {} # for query answers
        outlist = [] # what if there are duplicate q's? Guess it's fine...

        for q in newq:
            while i < len(intervals) and intervals[i][0] <= q:
                l = intervals[i][0]
                r = intervals[i][1]
                heapq.heappush(minHeap, (r - l + 1, r)) # want min length & earliest end
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap) # not valid interval

            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1

        for q in queries:
            outlist.append(res.get(q, -1)) # is this even needed anymore?

        return outlist


        '''

        # one idea brute force is like, for every possible query point j
        # we store hashmap key query val : len of shortest including it
        # and then update that hashmap accordingly

        # runetime could be len(intervals) * len(longest interval)
        # O(nlogn + mlogm) desired runtime means sorting both?
        # O(m + n) space means storing one spot per interval...

        # brute force works, but times out for largest test cases

        hm = {}

        for i, j in intervals:
            for k in range(i, j+1):
                if k not in hm:
                    hm[k] = j - i + 1
                else:
                    hm[k] = min(hm[k], j - i + 1)

        outlist = []
        for q in queries:
            outlist.append(hm.get(q, -1))
        return outlist

        '''

        