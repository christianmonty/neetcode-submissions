class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        # I had right intuition do DP parts in this solution but needed to peek at solution,
        # particularly for Suffix Sums part and min-max optimization part

        M = 1 # this denotes upper mound, x is the optional index take, since x can be up to 2M
        dp = [[[0 for _ in range(2)] for _ in range(2 * len(piles) + 1)] for _ in range(len(piles) + 1)]
        # we'll do column as x taken, row as index. Would be upper triangular matrix

        # this takes in next index to check, and m to use, and a score returned (for Alice)
        # we can't denote which x to use in future cases via recursive call, it's up to optimal actor
        def recurse(index: int, m: int, alice: bool) -> int:
            if index >= len(piles):
                return 0
            subtotal = 0
            if (2 * m) >= len(piles) - index: # might as well take all the rest
                # accumulate options into subtotal and return
                t = index
                while t < len(piles):
                    subtotal += piles[t]
                    t += 1
                if alice:
                    dp[index][m][alice] = subtotal # set for all m's or no?
                    return subtotal
                return 0

            if dp[index][m][alice]:
                return dp[index][m][alice]
            
            # else, now we need to try 1 step, 2 step, 3 step all the way up to M steps
            x = 1
            maxcount = 0 if alice else float('inf') # if Bob
            while x <= 2 * m:
                subtotal = 0
                t = 0
                temp = 0
                while t < x and index + t < len(piles):
                    subtotal += piles[index + t]
                    t += 1
                if index + x <= len(piles):
                    temp = recurse(index + x, max(m, x), not alice)
                    if alice:
                        maxcount = max(maxcount, subtotal + temp)
                    else:
                        maxcount = min(maxcount, temp) # if Bob's turn, minimize Alice's total
                x += 1
            dp[index][m][alice] = maxcount
            return maxcount


        return recurse(0, 1, True)