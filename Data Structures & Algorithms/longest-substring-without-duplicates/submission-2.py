class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        length = 0
        templength = 0
        first = 0

        for i in range(0, len(s)):
            if s[i] in hm: #already
                before = hm[s[i]]
                while first <= before:
                    hm.pop(s[first])
                    first += 1
                    templength -= 1
            hm[s[i]] = i
            templength += 1
            if templength > length:
                length += 1
                

        return length     
        
        
        














        
        
        
        
        
        
        
        
        
        
        
        
        
        
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