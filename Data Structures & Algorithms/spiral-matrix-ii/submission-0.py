class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # if right, go right [vertical, horizontal]
        ddir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # if space is not taken and not out of bounds, keep in same direction

        arr = [[0 for _ in range(n)] for _ in range(n)]

        def recurse(i: int, j: int, direction: int, step: int):
            if arr[i][j] == 0:
                arr[i][j] = step
                step += 1
                if step > n * n:
                    return # stop recursing

            up, right = ddir[direction]
            newi, newj = i + up, j + right
            if newi < 0 or newi >= len(arr) or newj < 0 or newj >= len(arr[0]) or arr[newi][newj] != 0:
                recurse(i, j, (direction + 1) % 4, step)
            else:
                recurse(newi, newj, direction, step)
                

        recurse(0, 0, 0, 1)
        return arr