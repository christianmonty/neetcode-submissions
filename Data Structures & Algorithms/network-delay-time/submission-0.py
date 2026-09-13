from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # shortest path to ALL nodes, does that mean Floyd-Warshall?
        # maybe we add new nodes to a queue, then mark as visited or update length of shortest path to a hm?
        # no negative edges, so I guess can't have any infinite loops
        # wait no shortest path from one node to all nodes is still Djkstra's, since FW is all to all...

        # ok maybe we do a hashmap from node # -> list of nodes
        # then pop off priority queue, process any neighbors, make value in pq the min of to node + edge, existing
        # if node visited, skip processing again (don't add to pq again)
        # then at final node, it must be return that time. BUT if still unvisited nodes (len(visited) < n) return -1

        # Below is my attempt at implementing Djkstra's for this problem...

        visited = set()
        hm = defaultdict(list)
        pq = [[0, k]] # we start at k, in format [distance, node #]
        # must be double array since we want this to be our first entry, not 2 separate entries
        heapq.heapify(pq)
        largest = 0

        for t in times:
            hm[t[0]].append([t[1], t[2]])

        while pq:
            # invariant is once a node is taken off pq, we've found shortest route to it
            # another takeaway is last node to get off pq, must have furthest distance 
            dist, node = heapq.heappop(pq)

            if node in visited:
                continue
            
            if dist > largest:
                largest = dist
            
            visited.add(node)

            for dest, edge in hm[node]:
                if dest not in visited:
                    heapq.heappush(pq, [dist + edge, dest]) # another option, could be larger but won't be visited
        
        return largest if len(visited) == n else -1


        