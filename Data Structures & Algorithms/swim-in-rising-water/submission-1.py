import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # start at time t = 0, with no water level
        # as t increases, water level across entire grid keeps rising too...
        # can swim horizontally or vertically between adjacent squares if original elevation of both squares is
        # <= water level at time t. # starting from top left, return min amount of time to reach bottom right
        # can you only swim one cell per step? Or can you swim the whole way once a path is clear...?

        # feels kind of like DFS in that just have to reach the bottom & return True
        # or Djkstra's, but just stop when reach final node (bottom right)

        # what do we want to store in pq? the cost to get to that node which is value at cell + original cost
        # also want to store i, j in case we've found the end
        # we don't need adjacency hm, we can use visited which means we've processed index (popped from pq already), invariant is that would have been the min

        # below Djkstra's implementation works, but runs out of time for final test cases
        visited = set()
        pq = []
        directs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        heapq.heappush(pq, (grid[0][0], 0, 0))

        while pq:
            cost, r, c = heapq.heappop(pq)

            # visited.add((r, c))
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return cost

            for o, p in directs:
                nr = r + o
                nc = c + p
                if 0 <= nr <= len(grid) - 1 and 0 <= nc <= len(grid[0]) - 1 and (nr, nc) not in visited:
                    heapq.heappush(pq, (max(grid[nr][nc], cost), nr, nc)) # add any new potential paths
                    visited.add((nr, nc)) # why add here instead?? Is invariant this must be shortest path??

        return -1
        

            

