import heapq

from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        hq = []
        heapq.heapify(hq)

        counter = Counter(tasks)
        for c in counter.values():
            # this works since we don't need the actual letter it represents!
            heapq.heappush(hq, -c)
        
        deq = deque()

        time = 0
        while hq or deq:
            time += 1

            if hq:
                temp = heapq.heappop(hq)
                temp += 1
                if temp: # o/w it's off both hq and deq
                    deq.append((temp, time + n))
            while deq and deq[0][1] == time:
                putback = deq.popleft()
                heapq.heappush(hq, putback[0])

            
        return time



























        ''' initial way of solving, using hm, list and pq
        hm = {} # probably unique count way to initialize

        for t in tasks:
            hm[t] = hm.get(t, 0) + 1
        
        pq = []
        heapq.heapify(pq)
        coolingbox = []

        for key in hm:
            heapq.heappush(pq, [-hm[key], 0, key])

        count = 0
        while pq or len(coolingbox) > 0:
            if pq:
                nxt = heapq.heappop(pq)
                nxt[0] += 1
                if nxt[0] < 0:
                    nxt[1] = n + 1 # because of below work, will knock time automatically
                    coolingbox.append(nxt)

            for item in coolingbox:
                item[1] -= 1
            
            for item in coolingbox:
                if item[1] == 0:
                    coolingbox.remove(item)
                    heapq.heappush(pq, item)
            count += 1

        return count
        '''
            

        


