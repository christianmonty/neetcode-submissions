class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # I guess ideally we want to have priority q of height differences, and use ladders on those
        # but if # ladders < size of pq array, have to spend bricks initially so we do that
        # if we run out of bricks and len(heap) > ladders (must be if bricks are below 0, return i for that index
        # then aren't we confusing jump height (maybe from back forward) with progress from index 0?

        # had to peek at Solution here since was confused between tracking trip from beginning & final building get to
        pq = []

        for i in range(len(heights) - 1):
            dist = heights[i + 1] - heights[i]
            if dist <= 0:
                continue
            heapq.heappush(pq, dist)
            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)
            if bricks < 0:
                return i
        return len(heights) - 1