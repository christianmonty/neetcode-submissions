class Solution:
    def partition(self, s: str) -> List[List[str]]:
        outlist = []
        subset = []

        def isPalindrome(w: str) -> bool:
            i, j = 0, len(w)-1
            while i < j:
                if w[i] != w[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i):
            if i >= len(s):
                for strings in subset:
                    if not isPalindrome(strings):
                        return
                outlist.append(subset.copy())
                return

            if subset:
                n = len(subset)
                temp = subset[n-1]
                subset[n-1] = temp + s[i]
                dfs(i+1)
                subset[n-1] = temp           
            
            subset.append(s[i])
            dfs(i+1)
            if subset:
                subset.pop(len(subset)-1)


        dfs(0)
        return outlist


        
            