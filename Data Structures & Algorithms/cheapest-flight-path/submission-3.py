import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)] # for each airport to have adjacency list
        # don't need hm since 0 through n - 1

        for f in flights:
            adj[f[0]].append([f[1], f[2]]) # airport a can fly to b, at a cost of price
        
        pq = [[0, src, 0]] # this is cost to get to, airport, and k value
        # heapq.heapify(pq) # is this necessary...? Don't need apparently since single item

        visited = set()

        while pq:
            totalcost, airport, kval = heapq.heappop(pq)

            if kval > k + 1:
                continue
            
            if airport == dst:
                return totalcost

            visited.add((airport, kval))

            for dest, nextcost in adj[airport]:
                if (dest, kval) not in visited:
                    heapq.heappush(pq, [totalcost + nextcost, dest, kval + 1])

        return -1