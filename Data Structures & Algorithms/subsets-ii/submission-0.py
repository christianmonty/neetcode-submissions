class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        outlist = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                temp = subset.copy()
                temp.sort()
                if temp not in outlist:
                    outlist.append(temp)
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)


        dfs(0)
        return outlist