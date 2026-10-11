import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        # this proposed solution of mine would use 3 queues
        # 1. for free rooms, 2. for soonest meeting, 3. for earliest end (for next free room)

        rooms = [[i, 0] for i in range(0, n)] # 2nd to track # meetings
        heapq.heapify(rooms)

        earlystart = [[m[0], m[1]] for m in meetings]
        heapq.heapify(earlystart)
        soonend = []

        while earlystart:
            nextstart, nextend = heapq.heappop(earlystart)

            while soonend and soonend[0][0] <= nextstart:
                lastend, roomnum, laststart, lastcount = heapq.heappop(soonend)
                heapq.heappush(rooms, [roomnum, lastcount])

            # check rooms for which end time are <= nextstart and add back to rooms!

            if rooms:
                roomnum, lastcount = heapq.heappop(rooms)
                heapq.heappush(soonend, [nextend, roomnum, nextstart, lastcount + 1])
                # change order of soonend so it's sorted by nextend and then roomnum
            else:
                # must incrmeent nextend and nextcount
                lastend, roomnum, laststart, lastcount = heapq.heappop(soonend) # assumes not empty
                heapq.heappush(soonend, [lastend + (nextend - nextstart), roomnum, lastend, lastcount + 1])
        
        # invariant is should have full rooms now (or maxed out). So dump back into rooms...
        while soonend:
            laste, roomnum, lasts, endcount = heapq.heappop(soonend)
            heapq.heappush(rooms, [roomnum, endcount])

        counts = []
        while rooms:
            roomnum, endcount = heapq.heappop(rooms)
            heapq.heappush(counts, [-endcount, roomnum])

        return counts[0][1]
