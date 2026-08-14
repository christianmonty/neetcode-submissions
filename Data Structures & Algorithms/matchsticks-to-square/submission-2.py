class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # note the sum of all lengths % 4 must == 0, aut-reject if not
        # we actually know more than that, we know each of 4 sides must == lens / 4...
        # so perhaps the backtracking is iterate over all matchsticks
        # try backtrack fwd on slot 1, then remove & try 2, then 3, 4
        # with the backtrack recursive call being advance an index
        # since matchsticks is not long, we can do this recursion
        # and basically 
        # when you get to final index, if fits perfectly, as do other index, ret True
        # otherwise at final index and doesn't fit return False
        # figure out if sides should be copied everywhere or which scope
        # only need to ITERATE over the sides to add, but not index in matchstick since can call next one via passing to function

        # Optimization trick #1, fails faster when an option is impossible
        matchsticks = sorted(matchsticks, reverse=True) # solution trick to fill sides earlier...
        
        total = 0
        for m in matchsticks:
            total += m
        if total % 4 != 0:
            return False
        sidelen = total / 4 # should work
        sidesarr = [0] * 4

        def backtrack(index: int, sides: List[int]) -> bool:
            if index == len(matchsticks): # base case, return recursion
                for s in sides:
                    if s != sidelen:
                        return False
                return True
            
            for i, val in enumerate(sides):
                # Optimization 3: Just check paths when not overflowing
                if sides[i] + matchsticks[index] <= sidelen:
                    sides[i] += matchsticks[index]
                    retval = backtrack(index + 1, sides)
                    sides[i] -= matchsticks[index]
                    if retval:
                        return True
                # Optimization 3: if this side is empty, all future sides must be too. Since for all levels
                if sides[i] == 0:
                    return False
            
            return False

        
        return backtrack(0, sidesarr)


            

            
