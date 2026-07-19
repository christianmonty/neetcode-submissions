class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isP(w: str) -> bool:
            if len(w) <= 1:
                return True
            f, l = 0, len(w) - 1
            while f < l:
                if w[f] != w[l]:
                    return False
                f += 1
                l -= 1
            return True

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isP(s[i:j+1]):
                    count += 1

        return count