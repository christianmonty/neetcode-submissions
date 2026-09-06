class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # until there is only 1 party left (one hm empty)
        # once one hashmap empty, other one wins on next term
        # if odd #, majority will [always] win. If even, one who goes first will always win

        # always try to solve first, even inefficiently then can reduce later
        # we could do 2 pointers, one on next R, one on next D...

        dp = [True for _ in range(len(senate))] # can probably reduce space later

        R = 0
        D = 0

        for x in range(len(senate)):
            if senate[x] == 'R':
                R += 1
            else:
                D += 1

        i = j = 0
        while i < len(senate) and senate[i] != 'R':
            i += 1 # loop around with mod, check passed left?
        while j < len(senate) and senate[j] != 'D':
            j += 1
        # do we need to check if i o j is out of bounds

        k = 0
        while R and D:
            # greedily take the next most "R" or "D". This implicitly does the turn
            if dp[k]:
                if senate[k] == 'R':
                    dp[j] = False
                    D -= 1
                    if D <= 0:
                        return "Radiant"
                elif senate[k] == 'D':
                    dp[i] = False
                    R -= 1
                    if R <= 0:
                        return "Dire"
                j = (j + 1) % len(senate)
                i = (i + 1) % len(senate)

                while senate[j] != 'D' or not dp[j]:
                    j = (j + 1) % len(senate)
                while senate[i] != 'R' or not dp[i]:
                    i = (i + 1) % len(senate)
            k = (k + 1) % len(senate) # skip to next k either way


        return "Radiant" if R else "Dire"

        

            # NOTE: each letter wants to take rights of NEXT APPROACHING letter to minimize other team's impact

            # if i in game, decrease the other
