class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # invariant looks like # sides that touch water == perimeter

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perim = 0
        visited = set() # maybe cleanest vs. full copied array
        # copygrid = [0 for _ in grid[0]] for _ in grid:  # something like this to copy entire array

        def isValid(r: int, c: int) -> bool:
            if (r >= 0 and r < len(grid)) and (c >= 0 and c < len(grid[0])) and grid[r][c]: # double duty here
                return True
            return False

        def dfs(r: int, c: int):
            nonlocal perim # since int is immutable
            visited.add((r, c))

            for d in dir:
                row = r + d[0]
                col = c + d[1]
                if (row, col) not in visited:
                    if isValid(row, col):
                        dfs(row, col)
                    else:
                        perim += 1

        # find first grid elem == 1 and call dfs there
        # there is def cleaner way to call these
        for idr, row in enumerate(grid):
            for idc, col in enumerate(row):
                if grid[idr][idc] == 1:
                    dfs(idr, idc)
                    return perim
        