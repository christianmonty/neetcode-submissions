class Solution:
    def reverseBits(self, n: int) -> int:

        if not n:
            return n
        res = num = 0

        while n:
            digit = n & 1
            res |= digit
            n >>= 1
            res <<= 1
            num += 1
        left = 32 - num - 1
        return res << left if left > 0 else res >> -left


        