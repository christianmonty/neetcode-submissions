from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # min amount of time to reach all nodes from single node is shortest path
        # we can have a priority queue with shortest next path remaining
        pq = [] # for next shortest path
        adj = defaultdict(list) # this is to track node a -> what is it connected to
        visited = set() # for nodes we've seen we can check if == n at end

        # add original node with path cost 0 to heapq. Format: (cost, node)
        # we can lazily add every viable path to pq since if dupicates, we just ignore if visited

        # check also if there's cleaner way to implement all of this...

        for source, target, time in times:
            adj[source].append([target, time])
        
        heapq.heappush(pq, (0, k))
        maxcost = 0

        while pq:
            lastcost, node = heapq.heappop(pq)
            if node in visited:
                continue

            maxcost = max(lastcost, maxcost)

            visited.add(node)

            for neighbor, cost in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (lastcost + cost, neighbor))
        
        return -1 if len(visited) < n else maxcost

        