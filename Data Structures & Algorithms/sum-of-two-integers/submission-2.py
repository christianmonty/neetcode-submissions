class Solution:
    def getSum(self, a: int, b: int) -> int:
        #how to know where to start iterating?
        #final digit but how to get there

        n = 32
        total = res = carry = 0
        for i in range(0, n):
            p1 = (a >> i) & 1
            p2 = (b >> i) & 1

            if carry:
                if p1 & p2:
                    res = 1
                    carry = 1
                elif p1 | p2:
                    res = 0
                    carry = 1
                else:
                    res = 1
                    carry = 0
            else:
                if p1 & p2:
                    carry = 1
                else:
                    carry = 0
                res = p1 ^ p2

            res <<= i
            total += res
            res = 0

        if total >> 31 & 1:
            total = ~(total ^ 0xFFFFFFFF)
        
        return total

        