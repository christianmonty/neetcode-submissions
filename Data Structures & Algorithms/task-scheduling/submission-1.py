import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        hm = {}
        hs = set()
        count = 0

        for t in tasks:
            if t in hm:
                hm[t] += 1
            else:
                hm[t] = 1

        for key in hm:
            if hm[key] > 1:
                maxhval = -hm[key]
                temp = (maxhval, key)
                heapq.heappush(pq, temp)
            else:
                hs.add(key)
        
        while pq:
            k = 0
            tempq = []
            while k <= n:
                if pq:
                    (c1, let1) = heapq.heappop(pq)
                    tc1 = -c1
                    if tc1 > 0:
                        heapq.heappush(tempq, (c1+1, let1))
                elif hs:
                    hs.pop()
                count += 1
                k += 1
            while tempq:
                (c2, let2) = heapq.heappop(tempq)
                tc2 = -c2
                if tc2 > 1:
                    heapq.heappush(pq, (c2, let2))
                else:
                    hs.add(let2)
        
        if hs:
            count += len(hs)

        return count
