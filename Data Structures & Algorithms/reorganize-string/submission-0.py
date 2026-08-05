from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        # I think this is similar in style to "Longest Happy String" in that want to greedy allocate by count
        # Steps:
        # 1. Put counts in hm, then put hm items in pq
        # use Counter instead of hm
        # want maxheap so do negative values
        hm = Counter(s)
        pq = []

        for index, val in hm.items():
            pq.append((-val, index)) # for -num, letter
        
        heapq.heapify(pq)
        outs = ""

        while pq:
            # so the trick is we pop one, if it's last letter in outstring, put it aside, pop another and put back
            top = heapq.heappop(pq)
            if outs and outs[-1] == top[1]: # only have to compare to previous character, invariant is rest of string is valid
                # then pop another and put top back
                temp = top
                if pq:
                    top = heapq.heappop(pq)
                    heapq.heappush(pq, temp)
                else:
                    return "" # double check this
            outs = outs + top[1]
            top = (top[0] + 1, top[1])
            if top[0]:
                heapq.heappush(pq, top)
        
        return outs



        