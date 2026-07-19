class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #wild new DP esque idea is as follows. Have a queue (for levels) and an array (for new start index)
        #but we can use 2 arrays and delete the beginning one end of each turn
        if not s:
            return False

        queue = []
        done = [0] * len(s)
        hs = set()
        maxl = 0

        for w in wordDict:
            hs.add(w)
            if len(w) > maxl:
                maxl = len(w)
        f = 0

        while f < len(s):

            for i in range(f, min(f+maxl, len(s))):
                w = s[f:i+1]
                if w in wordDict: # all that matters is length, not actual word!
                    if i == len(s) - 1:
                        return True
                    if i + 1 not in queue and not done[i+1]:
                        queue.append(i+1) # new starting point

            if queue:
                f = queue.pop()
                done[f] = 1
            else:
                return False
        
        
        
        
        
        
        #another idea, start with end. Then try front and i:end, front and i and end, front:i and end. Pattern speaking to me
        #if any of these return True, return True
        #recurse down, so if end is "" return true, if not then it iterates across that?
        #how to we save on iterative searches? Two linear passes from front & back first and store 1 in array if passes, 0 o/w

        # if any of below are true, set == 1
        #return dp[0:front+1] && dp[i] && dp[end] || dp[front:i+1] && dp[end] || dp[front] && dp[i:end+1] 

        '''
        if not s:
            return False
        subDict = []
        end = len(s) - 1
        last = end
        first = 0
        sset = set()
        for w in wordDict:
            sset.add(w)
            if w in s:
                subDict.append(w)
        subDict.sort(key = len, reverse = True)

        while first <= end:
            while s[first:last+1] not in sset:
                last -= 1
                if last < first:
                    return False
            first = last + 1
            last = end

        return True
        '''