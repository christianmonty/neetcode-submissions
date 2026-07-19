class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outlist = []

        def dfs(i, subset):
            if i >= len(nums):
                outlist.append(subset.copy())
                return
            
            for j in range(0, len(subset)+1):
                subset.insert(j, nums[i])
                dfs(i+1, subset)
                subset.pop(j)



        dfs(0, [])
        return outlist