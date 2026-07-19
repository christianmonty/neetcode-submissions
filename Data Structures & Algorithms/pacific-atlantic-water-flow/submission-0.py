class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return None
        rows = len(heights) - 1
        cols = len(heights[0]) - 1
        directions = [[-1, 0], [0, -1], [1,0], [0, 1]]

        hsF = []
        hsP = set() #let True == Pacific
        hsA = set() #left False == Atlantic

        def isValid(T: bool, row: int, col: int) -> bool:
            if col < 0 or col > cols or row < 0 or row > rows:
                return False
            
            if T and (row, col) in hsP or not T and (row, col) in hsA:
                return False

            return True

        def recurse(T: bool, row: int,  col: int):                
            if T:
                hsP.add((row, col))
            else:
                hsA.add((row, col))
            for d in directions:
                a = d[0] + row
                b = d[1] + col
                if isValid(T, a, b):
                    if heights[a][b] >= heights[row][col]:
                        recurse(T, a, b)
        

        for i in range(0, cols + 1):
            if isValid(True, 0, i):
                recurse(True, 0, i)
            if isValid(False, rows, i):
                recurse(False, rows, i)
        for i in range(0, rows + 1):
            if isValid(True, i, 0):
                recurse(True, i, 0)
            if isValid(False, i, cols):
                recurse(False, i, cols)
        
        for item in hsP:
            if item in hsA:
                hsF.append(item)

        return hsF

