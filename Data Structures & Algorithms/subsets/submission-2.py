class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outlist = []
        hs = set()

        def dfs(subs: List[int], count: int):
            if count == len(nums):
                newlist = sorted(subs)
                if tuple(newlist) not in hs:
                    hs.add(tuple(newlist))
                    outlist.append(newlist)
                return

            
            subs.append(nums[count])
            dfs(subs, count + 1)
            subs.pop()
            dfs(subs, count + 1)
            return

        dfs([], 0)
        return outlist


        