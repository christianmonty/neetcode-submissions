class Solution:
    def minEnd(self, n: int, x: int) -> int:

        # trying the most efficient solution here, O(1) storage
        # iterate through the zero bits of x and the bits of (n-1) not n since n-1 bits after
        res = x
        i_x = i_n = 1

        while i_n <= n - 1: # increments n digits (logn) not n numbers (O(n))
            if i_x & x == 0: # check each digit bit of x, we can fill if is 0
                if i_n & (n-1):
                    res = res | i_x # set in res the i_x digit bit as 1, else set as zero
                i_n = i_n << 1 # increment i_n since we filled in a digit
            i_x = i_x << 1 # passed another digit of x

        # how is there no edge cases if go 64 digits with i_x?

        return res



        ''' 
        # brute force method, fails for large N

        total = 1 # this is tracking vs. n, the other values don't matter...

        i = x + 1
        while total < n:
            if i & x == x:
                total += 1
                if total == n:
                    return i
            i += 1
        
        return x

        # basically start wih x as first # in array, then add a one with a leftshift each time (since will AND) out
        # but wait what if n is REALLY large? Each i + 1 must be greater than i?
        # but can also right shift the 1 like from 2 -> 3...
        # but wait 11 -> 15 means it's fine since 3 0's out other digits
        # all the other #'s that use 3 as a binary base could work, just must be in order
        # so iteration could test, increment by one and check that AND still equals original x...
        '''