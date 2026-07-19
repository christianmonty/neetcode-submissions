class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        l = r = 0
        shortest = ""
        shortlen = float("infinity")
        ht = {}
        hs = {}


        for i in range(0, len(t)):
            ht[t[i]] = ht.get(t[i], 0) + 1

        have, need = 0, len(ht)

        # solution in my own words
        for r in range(len(s)):
            c = s[r] # for next char in s
            hs[c] = hs.get(c, 0) + 1 # to increase count

            if c in ht and ht[c] == hs[c]:
                have += 1

            while have == need:
                if (r - l + 1) < shortlen:
                    shortest = s[l:r+1]
                    shortlen = r - l + 1
                
                hs[s[l]] -= 1
                if s[l] in ht and ht[s[l]] > hs[s[l]]:
                    have -= 1
                l += 1
            
        return shortest if shortlen != float("infinity") else ""
        
        
        '''
        # initial attempt
        while r < len(s):
            if s[r] not in ht and not hs:
                r += 1
                l = r
            elif s[r] not in ht:
                r += 1
            else:
                hs[s[r]] = hs.get(s[r], 0) + 1
                if hs == ht:
                    shortest = s[l:r+1]
                    break # found window
                r += 1

        # now we have window, moving to expand stage
        # first look for initial letter forward
        while r < len(s):
            if s[r] != s[l]:
                r += 1
            else:
                l += 1
                while s[l] not in hs:
                    l += 1
                shortest = s[l:r+1]
        
        return shortest
        '''
    