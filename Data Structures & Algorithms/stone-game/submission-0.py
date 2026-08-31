class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        total = 0
        for p in piles:
            total += p

        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))] # size of indices row/col
        # oh may instead it should be (indices, alice or bob
        # as in hm[(turn, alice)] and wait till be get to total turns? indices seems cleaner

        # play around with the math here on paper to see if there's a clever trick...
        def recurse(first: int, last: int) -> int:
            if first == last - 1:
                # must be at end of the game
                if piles[first] >= piles[last]:
                    dp[first][last] = piles[first]
                    return piles[first]
                dp[first][last] = piles[last]
                return piles[last]

            if dp[first][last]:
                return dp[first][last]
            
            else:
                takefirst = piles[first] + recurse(first + 1, last - 1)
                takelast = piles[last] + recurse(first + 1, last - 1) # not fully accurate but approx

                if takefirst >= takelast:
                    dp[first][last] = takefirst
                    return takefirst
                else:
                    dp[first][last] = takelast
                    return takelast
        
        aliceScore = recurse(0, len(piles) - 1) # this just returns total amount to win but not who wins...
        bobScore = total - aliceScore

        return aliceScore >= bobScore


            

            

                                        