class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # 4 cases:
        # 1. interval i in intervals completely captured by toBR, discard it
        # 2. interval i in intervals back half overlaps, truncate front tBR - 1
        # 3. interval i in intervals front half overlaps, truncate back tBR + 1
        # 4. interval i in intervals toally outside of tBR range

        outlist = []
        # front, end in intervals
        for f, e in intervals:
            if f >= toBeRemoved[0] and e <= toBeRemoved[1]:
                # skip
                pass
            elif f < toBeRemoved[0] and (toBeRemoved[0] <= e <= toBeRemoved[1]):
                # truncate back off
                outlist.append([f, toBeRemoved[0]])
            elif e > toBeRemoved[1] and (toBeRemoved[0] <= f <= toBeRemoved[1]):
                outlist.append([toBeRemoved[1], e])
            elif f < toBeRemoved[0] and e >= toBeRemoved[1]:
                outlist.append([f, toBeRemoved[0]])
                outlist.append([toBeRemoved[1], e])
            else:
                outlist.append([f, e])
        
        return outlist