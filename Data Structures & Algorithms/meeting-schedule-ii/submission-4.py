"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#idea of this solution is basically 2 pointers, after interval sort
#I figured 2 pointers but I did not figure a start array & end array

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda i: i.start)

        begin, finish = [], []
        for index, obj in enumerate(intervals):
            begin.append(obj.start)
            finish.append(obj.end)
        begin.sort()
        finish.sort()

        p1 = p2 = tempc = maxc =  0

        while p1 < len (begin):
            if begin[p1] >= finish[p2]:
                tempc -= 1
                p2 += 1
            else:
                p1 += 1
                tempc += 1
                if tempc > maxc:
                    maxc = tempc
        return maxc
        