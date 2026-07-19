from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        newints = sorted(intervals)
        q = deque()
        for n in newints:
            q.append(n)
        outlist = []

        # iterate over pairs. if overlap, pull min of first item, max of second, move i to j + 1
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()

            if b[0] > a[1]: # happy path
                outlist.append(a)
                q.appendleft(b)
            else: # there's overlap, must put back into queue
                newstart = min(a[0], b[0])
                newend = max(a[1], b[1])
                q.appendleft([newstart, newend])
        if q:
            outlist.append(q.popleft())

        return outlist