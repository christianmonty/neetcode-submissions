class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        outlist = []
        templist = []

        def checkDepth(val: int, newlist: List[int]) -> bool:
            if val < 0:
                return False
            elif val == 0:
                sortedl = sorted(newlist)
                if sortedl not in outlist:
                    outlist.append(sortedl)
                    return True
                return False
            for item in nums:
                tlist = newlist.copy()
                tlist.append(item)
                res = checkDepth(val - item, tlist)
            
        
        checkDepth(target, templist)
        return outlist