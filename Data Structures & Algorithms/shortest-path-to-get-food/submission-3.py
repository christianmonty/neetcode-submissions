from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        # this looks like BFS with shortest depth to find food or none
        # queue will be pop it, = symbol, i, j, depth. if food, return depth
        # else add index to visited and then..
        # and enqueue depth + 1 for all valid directions not in visited nor a wall
        # we will start with the only starting position maybe we get iteratively? if possible

        visited = set() # for tuples visited

        starti = startj = 0
        done = False
        for i in range(len(grid)):
            if done:
                break
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    starti = i
                    startj = j
                    done = True
                    break

        q = deque()
        q.append(("*", starti, startj, 0))
        visited.add((starti, startj))
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while q:
            sym, i, j, depth = q.popleft()
            if sym == '#':
                return depth
            for up, right in dir:
                newr = up + i
                newc = right + j
                if newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(grid[0]) and (newr, newc) not in visited and grid[newr][newc] != 'X':
                    q.append((grid[newr][newc], newr, newc, depth + 1))
                    visited.add((newr, newc))
        
        return -1
