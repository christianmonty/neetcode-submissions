class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [[0,1], [1,0], [0,-1], [-1,0]]

        def recurse(r: int, c: int, oldcol: int, newcol: int):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != oldcol:
                return
            image[r][c] = newcol
            for nr, nc in dir:
                recurse(r + nr, c + nc, oldcol, newcol)
        
        if color != image[sr][sc]:
            recurse(sr, sc, image[sr][sc], color)
        return image

        