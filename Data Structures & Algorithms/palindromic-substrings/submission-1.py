class Solution:
    def countSubstrings(self, s: str) -> int:
        #two pointers approach
        res = 0

        for i in range(len(s)):
            l, r = i, i
            #for odd # palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            #for even # palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res


        '''
        #brute force, worked but not good enough runtime
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
        '''