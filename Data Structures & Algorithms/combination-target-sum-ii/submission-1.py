class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, res, t):
            if t == target:
                temp = res.copy()
                temp.sort()
                if temp not in output:
                    output.append(temp)
                return
            if i >= len(candidates) or t > target:
                return
            res.append(candidates[i])
            dfs(i+1, res, t + candidates[i])
            res.pop()
            dfs(i+1, res, t)


        dfs(0, [], 0)
        return output