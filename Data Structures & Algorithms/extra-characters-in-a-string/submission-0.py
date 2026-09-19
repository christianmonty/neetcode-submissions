class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # want to extend words to longest as pos to minimize extra characters
        # but greedy may not work vs. bunch of small words
        # so might as well check dp, skip letter vs. include?
        # how do we incorporate a Trie here?




        # below is solved DP way, but point of this exercise is practice Tries

        # the dp way to think about it is for dp[i], I can check dp[i+1] + skip dp[i] return 1 + dp[i+1]
        # or I can take min of dp[i:j] + dp[j+1:end] for all j
        # or rather, if s[i:j] in dict, take min of dp[j] that fits
        # or try skipping and that's 1 + dp[i + 1]
        # set dp[i] to min found from there by either skipping or taking

        dp = [0 for _ in range(len(s)+1)]
        dp[len(s)] = 0
        i = len(s) - 1
        end = len(s)
        words = set(dictionary) # convert for O(1) lookup time

        while i >= 0:
            j = i + 1
            mmin = float('inf')
            while j < len(s) + 1:
                if s[i:j] in words:
                    mmin = min(mmin, dp[j])
                j += 1
            mmin = min(mmin, 1 + dp[i + 1]) # skip letter entirely
            dp[i] = mmin
            i -= 1
        
        return dp[0]