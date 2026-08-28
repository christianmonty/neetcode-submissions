class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)] # double check if need these

        def recurse(sum: int, index: int) -> int:
            if index >= len(coins) or sum > amount:
                return 0
            if sum == amount:
                return 1
            if dp[sum][index+1]:
                ret1 = dp[sum][index + 1]
            else:
                ret1 = recurse(sum, index + 1)
                if ret1:
                    dp[sum][index + 1] = ret1
            
            if sum + coins[index] <= amount and dp[sum + coins[index]][index]:
                ret2 = dp[sum + coins[index]][index]
            else:
                ret2 = recurse(sum + coins[index], index)
                if ret2:
                    dp[sum + coins[index]][index] = ret2
            return ret1 + ret2

        return recurse(0, 0)


        '''
        # this approach didn't work, wasn't efficient enough...

        # idea to memoize, if sum is 2, and already tried at index 2, then use that affect to increase count without another recursive call

        def recurse(sum: int, index: int):
            nonlocal count # so can modify it here
            if sum > amount:
                return
            if sum == amount:
                count += 1
                dp[index][sum] = 1 # is this not enough
                return
            while index < len(coins):
                if dp[index][sum]:
                    # already found path works
                    count += 1
                else:
                    # only now recurse
                    recurse(sum + coins[index], index)
                index += 1

        recurse(0, 0)
        return count

        '''



        # Below approach is me trying to do a proper 2D DP array vs. recursive solution at each step
        # my instinct is coins as rows, amount as cols
        # 1 is always 1
        # then a cell is top + left + if amount % coin == 0. Or maybe just left + amount % coin == 0
        # or it's value - coin == thing, check dp of that or something right since can use unlimited of eqach coin
        # combination since order doesn't matter
        # there's some order here even I can't yet quite articulate & grasp
        # then total ways for each value is sum of entire column for that value

        '''
        0 1 2 3 4
        1 1 1 1 1
        2 0 1 1 2
        3 0 0 1 1
        T 1 2 3 4
        '''

        # first fill row with 1
        # then fill next row starting from coin >= the value
        # drag from right, add on 1 if value % coin == 0 (besides for 1 row)
        # then total is accumulation of that value across coins?

        # dp = [[0 for _ in range(amount)] for _ in range(len(coins))] # col inside, row outside
        # do we need to add a zero row or zero col?

        