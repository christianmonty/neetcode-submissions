class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # for min # intervals to remove, want to remove LARGEST gaps if overlap with multiple intervals within
        # so one idea is sort(), will order by first then by second
        # could add to a max gap heap, but then not guarantee NEEDING to remove
        # sort, if two adjacent overlap (more than a common point) remove the larger gap (is this greedy, local opt?)
        # maybe add rest of intervals (to keep) to new array since cleaner?
        # how can we tell overlapping if sorted? if 1. a is subset of b, or b is subset of a..
        # if a[1] > b[0] - is this precise condition? Then compare gapa vs. gapb and keep smaller

        # initially I tried greedy always with shorter intervals, but this is not optimal. Need to evict later end time!!
        # non-intuitive solution, will need to repeat this problem later on

        ints = sorted(intervals)
        i, j = 0, 1
        outnum = 0
        while j < len(ints): # two pointers
            a, b = ints[i], ints[j]
            if a[1] > b[0]: # overlap detected
                if a[1] > b[1]: # depends on which one ends later
                    i = j
                    j += 1
                else:
                    j += 1
                outnum += 1
            
            else: # NO OVERLAP
                i = j
                j += 1
            
        
        return outnum


        