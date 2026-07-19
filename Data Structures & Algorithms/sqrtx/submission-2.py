class Solution:
    def mySqrt(self, x: int) -> int:
        # you could start with r at 1/2 x, l at 1. Calculate midpoint
        # then basically you don't want to overshoot, find largest int <= s.t. int * int <= x
        # ignore x = 0 for now, edge case

        if x == 0 or x == 1:
            return x

        l, r = 0, x // 2
        while l <= r:
            mid = (l + r) // 2
            exp = mid * mid
            if exp == x:
                return mid
            elif exp > x:
                r = mid - 1
            else:
                l = mid + 1
        return r # pattern here is that l*l will not exceed x
        