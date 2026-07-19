class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        p = n
        if n < 0:
            p = -n

        for i in range(0, p):
            res *= x
        if n < 0:
            return 1/res
        return res
        