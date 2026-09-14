import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # ok clearly this needs to be a min spanning tree
        # one thing we could do is calculate all possible edges O(n^2) space & time, add to pq
        # and then pop from pq, add edge if at least one point not yet in tree yet
        # greedily choose all the smallest edges first

        # below is prim's algorithm - but adding nodes to pq not edges, can't greedy global in tree must be for nodes in tree

        adj = [[] for _ in range(len(points))]

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # heapq.heappush(pq, (dist, tuple(points[i]), tuple(points[j])))

        mincost = 0
        visited = set()
        pq = [[0, 0]]
        heapq.heapify(pq)

        while pq:
            cost, index = heapq.heappop(pq)

            if index in visited:
                continue

            mincost += cost
            visited.add(index)

            for edge, neighbor in adj[index]:
                if neighbor not in visited:
                    heapq.heappush(pq, [edge, neighbor])

        return mincost



