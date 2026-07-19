class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # brute force way to solve is to put every possible prefix into a hashamp, return highest count

        # another option: just store length of longest common prefix or longest common, but not enough

        hm = {}
        for s in strs:
            for i in range(0, len(s)):
                prefix = s[:i+1]
                if prefix not in hm: # replace with cleaner way to check this via some library
                    hm[prefix] = 1
                else:
                    hm[prefix] += 1

        maxp = ""
        maxc = 0

        for p in hm:
            if hm[p] == len(strs):
                if len(p) > maxc:
                    maxc = len(p)
                    maxp = p

        return maxp
