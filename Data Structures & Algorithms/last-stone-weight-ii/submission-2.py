class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        # NOTE: this problem was tricky for me to grasp bc it's mathematical vs. a clever DP concept trick

        # since we know all stone weights are positive, can assume one half negative one half positive to combine
        # since abs() of a subtraction (difference) is same as negative half and positive half

        # because there are only max 30 stones, can iterate over them quickly & easily

        # Peaked at recursive solution conceptually to understand how to approach solving it

        # ok now let's figure out how to memoize this


        total = 0
        for s in stones:
            total += s
        target = total // 2


        # 0 to total as rows, all indexes as columns
        dp = {} # instead of the below so 0 doesn't throw us off
        # [[0 for _ in range(len(stones)+ 1)] for _ in range(total + 1)]

        def recurse(index: int, sum: int):
            if index >= len(stones) or sum > target:
                return abs(sum - (total - sum))

            if (sum, index + 1) in dp:
                skip = dp[(sum, index + 1)]
            else:
                skip = recurse(index + 1, sum)
                dp[(sum, index + 1)] = skip
            if (sum + stones[index], index + 1) in dp:
                take = dp[(sum + stones[index], index + 1)]
            else:
                take = recurse(index + 1, sum + stones[index])
                dp[(sum + stones[index], index + 1)] = take
            
            return min(skip, take)

        return recurse(0, 0)

       







        '''
        # my initial attempt, this was misguided, since it's too focused on hashing entire list

        # the repeated calls are if left with same set of #'s at given round, don't do duplicative recursion
        # instead do what, reference cached value for smallest possible value for smaller subset

        # figure out where to set the dp min

        # OH maybe should we pass this into the recursion?? Like here's min, here's a subarray
        hm = {} # where does 2D part come in if hash entire sublist...?

        def recurse(subs: List[int]) -> int:
            smin = float('inf')

            if len(subs) == 1:
                return subs[0]
            elif len(subs) < 1:
                return 0
            subs.sort() # can do efficiently since only 30 items max
            if tuple(subs) in hm:
                return hm[tuple(subs)] # tbd if keep this
            i = 0
            t = subs.copy()

            # try all possible choices -> at every step
            while i < len(subs):
                j = i + 1
                while j < len(subs):
                    num1 = t[i]
                    num2 = t[j]
                    if num1 == num2:
                        smash = 0
                    else:
                        smash = abs(num1 - num2)
                    t.remove(num1)
                    t.remove(num2)
                    if smash:   
                        t.append(smash)
                    t.sort()
                    if tuple(t) in hm: 
                        # if we've already tried this, just updatesmin if needed
                        smin = min(smin, hm[tuple(t)])
                    else:
                        # recurse
                        ret = recurse(t.copy())
                        smin = min(smin, ret)
                        # do we need to set the hm here too?
                        
                    t = subs.copy() # reset t at end
            # at end of this while loop, min value leftover should be placed in hm[tuple(subs)]
            hm[tuple(subs)] = smin # assuming this has been set correctly
        
        return recurse(stones)
        '''
        