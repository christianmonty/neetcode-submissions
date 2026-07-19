from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[0,1],[1,0], [-1,0],[0,-1]]
        minutes = [[0 for col in grid[0]] for row in grid]

        def isValid(r: int, c: int) -> bool:
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False
            return True

        def countRotten(r: int, c: int):

            q = deque()
            distance = 1
            for d in directions:
                row, col = r + d[0], c + d[1]
                if isValid(row, col) and grid[row][col] == 1 and (minutes[row][col] == 0 or minutes[row][col] > distance):
                    q.append([row, col])
            
            while q:
                qlen = len(q)

                while qlen:
                    row, col = q.popleft()
                    minutes[row][col] = distance # minutes to midnight for them lol
                    for d in directions:
                        r2, c2 = row + d[0], col + d[1]
                        if isValid(r2, c2) and grid[r2][c2] == 1 and (minutes[r2][c2] == 0 or minutes[r2][c2] > distance + 1):
                            q.append([r2, c2])
                    qlen -= 1
                distance += 1



        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    countRotten(i, j)

        maxtime = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # check impossibilty criteria and then return -1 if can't be met
                if grid[i][j] == 1 and minutes[i][j] == 0:
                    return -1
                maxtime = max(minutes[i][j], maxtime)

        return maxtime