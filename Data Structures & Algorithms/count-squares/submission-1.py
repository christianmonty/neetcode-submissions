from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.hm = defaultdict(int) # for quick lookups
        

    def add(self, point: List[int]) -> None:
        self.hm[(point[0], point[1])] += 1
        

    def count(self, point: List[int]) -> int:
        # presume we skip the point itself
        a = point[0]
        b = point[1]
        maxc = 0


        for index, val in self.hm.items():
            i = index[0]
            j = index[1]
            xdif = i - a
            ydif = j - b
            if index != (a, b):
                # if diagonal, check in between
                if abs(xdif) == abs(ydif):
                    corner1 = (a + xdif, b)
                    corner2 = (a, b + ydif)
                    if corner1 in self.hm and corner2 in self.hm:
                        # want the max count
                        maxc += self.hm[index] * self.hm[corner1] * self.hm[corner2]
        
        return maxc

        
