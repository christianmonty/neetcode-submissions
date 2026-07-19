class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outlist = []
        outlist.append([])

        for val in nums:
            newlist = []
            for cell in outlist:
                temp = cell.copy()
                temp.append(val)
                temp.sort()
                newlist.append(temp)
            for thing in newlist:
                if thing not in outlist:
                    outlist.append(thing)
        return outlist
