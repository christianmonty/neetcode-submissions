from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # idea: try moving one value at a time and adding to queue
        # queue is the level (# turns)
        # if find target, return that level (invariant is must be closest)
        # if deadend, don't add back to queue
        # else make all the 8 changes and if not in visited, add to queue

        visited = set()
        q = deque()

        for d in deadends:
            visited.add(d) # think can just add to visited
        
        if "0000" not in visited:
            q.append(("0000", 0))
            
        while q:
            temp = q.popleft()
            attempt = temp[0]

            if attempt == target:
                return temp[1]


            for i in range(4):
                newup = newdown = '0'
                if attempt[i] == '9':
                    newup = '0'
                else:
                    newup = str(int(attempt[i]) + 1)
                if attempt[i] == '0':
                    newdown = '9'
                else:
                    newdown = str(int(attempt[i]) - 1)

                moveup = attempt[0:i] + newup + attempt[i+1:4]
                movedown = attempt[0:i] + newdown + attempt[i+1:4]
                if moveup == target or movedown == target:
                    return temp[1] + 1
                if moveup not in visited:
                    visited.add(moveup)
                    q.append((moveup, temp[1] + 1))
                if movedown not in visited:
                    visited.add(movedown)
                    q.append((movedown, temp[1] + 1))
        return -1
