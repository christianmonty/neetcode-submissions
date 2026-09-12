import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # Below is my first implementation of Djkstra's algorithm...def practice again soon

        # key thing in Djkstra's is must initialize entire grid to infinity, except first cell at 0 since no abs difference
        # the genius of Djkstra's is the minheap property means if find a shorter path to node already in minHeap, will supercede that one...

        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        minHeap = [[0, 0, 0]] # max abs dif, row, col
        heapq.heapify(minHeap)
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c)) # means node has been proceesed, not calculated difference of

            if r == ROWS - 1 and c == COLS - 1:
                return diff

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue

                newDiff = max(diff, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minHeap, [newDiff, nr, nc])
            
            # for all nodes, in minHeap or not but not yet processed themselves
            # invariant in Djkstra's is if a node in processed, we've found shortest path

        return 0



        '''
        # below is my first attempt, which failed the 23 out of 24th edge case until I realized it was Djkstra's

        # do we want to pass visited set into this too or what?
        # pass in current val, new direction, return sum
        def recurse(visited: set(int), h: int, nr: int, nc: int) -> int:
            if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]):
                return float("inf") # should we mark as visited too? or mark this super large
            if nr == len(heights) - 1 and nc == len(heights[0]) - 1:
                return abs(heights[nr][nc] - h) # found final step

            visited.add((nr, nc))
            curval = heights[nr][nc]
            nextmove = abs(curval - h) # how we got to current cell - h is the history
            up = down = left = right = float("inf")
            if (nr - 1, nc) not in visited:
                up = recurse(visited, curval, nr - 1, nc)
            if (nr + 1, nc) not in visited:
                down = recurse(visited, curval, nr + 1, nc)
            if (nr, nc - 1) not in visited:
                left = recurse(visited, curval, nr, nc - 1)
            if (nr, nc + 1) not in visited:
                right = recurse(visited, curval, nr, nc + 1)
            visited.remove((nr, nc))

            return max(min(up, down, left, right), nextmove) # add how we get to final cell

        return recurse(set(), heights[0][0], 0, 0)
        '''
        