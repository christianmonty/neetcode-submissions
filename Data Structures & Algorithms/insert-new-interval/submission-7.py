class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        outlist = [] #didn't catch could use O(n) spae for output!
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            outlist.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0]) #tricky part, missed!! Running tallh
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        outlist.append(newInterval)

        while i < n:
            outlist.append(intervals[i])
            i += 1
        return outlist

        
    
        '''
        for index, item in enumerate(intervals):
            if newInterval[0] >= item[0] and (index == len(intervals)-1 or newInterval[0] <= intervals[index+1][0]):
                if index == len(intervals) - 1:
                    if newInterval[0] <= item[1]:
                        item[1] = max(item[1], newInterval[1])
                    else:
                        intervals.append(newInterval)
                    return intervals
                nxt = intervals[index+1]
                if newInterval[0] > item[1] and newInterval[1] < nxt[0]:
                    intervals.insert(index+1, newInterval)
                else:
                    if newInterval[0] <= item[1]:
                        item[1] = max(item[1], newInterval[1])
                    if item[1] >= nxt[0]:
                        item[1] = max(item[1], nxt[1])
                        intervals.pop(index+1)
                    temp = index+1
                    while temp < len(intervals):
                        if intervals[temp][0] <= item[1]:
                            item[1] = max(item[1], intervals[temp][1])
                            intervals.pop(temp)
                        temp += 1
                return intervals
            elif newInterval[0] < item[0]:
                if newInterval[1] < item[0]:
                    intervals.insert(index, newInterval)
                    return intervals
                temp = index
                item[0] = newInterval[0]
                item[1] = max(item[1], newInterval[1])
                temp += 1
                while temp < len(intervals) and item[1] >= intervals[temp][0]:
                    if item[1] >= intervals[temp][0]:
                        item[1] = max(item[1], intervals[temp][1])
                        intervals.remove(intervals[temp])
                        # am I screwing up temp index here somehow? Fails edge cases!!
                    temp += 1
                return intervals
        intervals.append(newInterval)
        return intervals

    # ugh need to keep merging right!
    '''