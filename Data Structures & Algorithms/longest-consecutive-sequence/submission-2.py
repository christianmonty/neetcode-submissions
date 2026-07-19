class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        beg = {}
        end = {}
        # intiliaze each with same value as each

        for item in nums:
            beg[item] = item
            end[item] = item
        for item in nums:
            if item - 1 in beg:
                beg[item] = beg[item - 1]
                end[beg[item -1]] = end[item]
            if item + 1 in beg:
                 beg[item + 1] = beg[item]
                 end[item] = end[item + 1]
        maxdif = 0
        for item in nums:
            tempdif = end[item] - beg[item]
            if tempdif > maxdif:
                maxdif = tempdif
        if nums: 
            return maxdif + 1
        else:
            return maxdif