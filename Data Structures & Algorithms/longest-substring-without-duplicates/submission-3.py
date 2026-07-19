class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = r = maxl = 0
        hs = set()

        while r < len(s):
            if s[r] not in hs:
                hs.add(s[r])
                maxl = max(maxl, r - l + 1)
                r += 1
            else:
                while s[r] in hs:
                    hs.remove(s[l])
                    l += 1

        return maxl







        
        
        
        
        
        






        
        
        
        
        
        
        
        '''
        hm = {}
        l, r = 0, 0
        best = 0

        while r < len(s):
            #first we don't know if r-l is valid
            if s[r] not in hm:
                hm[s[r]] = r
            else:
                l = max(hm[s[r]] + 1, l)
                hm[s[r]] = r
            best = max(best, r-l+1)
            r += 1
        return best
'''