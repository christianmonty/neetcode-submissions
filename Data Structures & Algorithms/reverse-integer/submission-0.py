class Solution:
    def reverse(self, x: int) -> int:
        
        def recurse(n: int, rev: int) -> int:
            if n == 0:
                return rev
            
            digit = n % 10
            n = n // 10
            rev = (rev * 10) + digit
            return recurse(n, rev)

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_number = recurse(x, 0)
        reversed_number *= sign

        if reversed_number > 2**31 - 1 or reversed_number < -2**31:
            return 0
        
        return reversed_number