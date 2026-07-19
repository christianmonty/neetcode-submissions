class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        outlist = []
        subset = []

        if not digits:
            return outlist

        def dfs(i):
            if i >= len(digits):
                ostring = ""
                for k in subset:
                    ostring = ostring + k
                outlist.append(ostring)
                return
            
            n = int(digits[i]) - 2
            for item in nums[n]:
                subset.append(item)
                dfs(i+1)
                subset.pop()
        
        dfs(0)
        return outlist

