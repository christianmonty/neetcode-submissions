class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # turbulent subarray means for that subarray, adjacent elements are either low high low high ....
        # or high low high low high ....

        # that makes me think 2 pointers where we check
        # that either every prev < cur, next < cur, then cur = next + 1, prev = next, next = cur->next
        # or prev > cur, next > cur

        # so the recursion could be try big, if memo return that. Else try all but first, or all but last? To skip one value
        # base case if down to two elements, return True since trivially the case. dp[1st index][2nd index]
        # oh wait why are we thinking 2D array? Do 1d array, start at beginning, then return True trivially, build up if 1st isn't part of turbulent array, skip to next.
        # or if we do 2D array memoization, at end just return max of col - row + 1....

        # let me try to do pure DP

        dp = [0 for _ in range(len(arr))]

        if len(arr) == 1:
            return 1
        elif len(arr) == 2:
            return 2 if arr[1] != arr[0] else 1


        dp[0] = 1
        if arr[1] != arr[0]:
            dp[1] = 2
        else:
            dp[1] = 1

        i = 2
        while i < len(arr):
            if arr[i] > arr[i - 1] and arr[i - 2] > arr[i - 1]:
                dp[i] = 1 + dp[i-1]
                # TBD
            elif arr[i] < arr[i - 1] and arr[i - 2] < arr[i - 1]:
                dp[i] = 1 + dp[i-1]
            elif arr[i] != arr[i - 1]:
                dp[i] = 2
            else:
                dp[i] = 1 # must be

            i += 1
        
        mmax = 0
        for val in dp:
            mmax = max(mmax, val)

        return mmax

