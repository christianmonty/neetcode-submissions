"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for index, obj in enumerate(intervals):
            if index < len(intervals) - 1:
                if obj.end > intervals[index+1].start:
                    return False
        return True