class Solution:
    def isHappy(self, n: int) -> bool:
        hs = set()
        hs.add(n)
        print(n)

        while n:
            subtotal = 0
            while n > 0:
                num = n % 10
                subtotal += (num**2)
                n //= 10
            if subtotal == 1:
                return True
            if subtotal in hs:
                return False
            #print(subtotal)
            hs.add(subtotal)
            n = subtotal

        return True
        