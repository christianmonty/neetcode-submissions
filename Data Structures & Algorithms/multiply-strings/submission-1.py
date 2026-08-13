class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # well we know that num - '0' gives actual number

        # build the numbers up digit by digit multiply by 10
        # then multiply, then convert back to string

        n1 = 0
        n2 = 0
        for c in num1:
            n1 = n1 * 10 + (ord(c) - ord('0'))
        for c in num2:
            n2 = n2 * 10 + (ord(c) - ord('0'))
        
        res = n1 * n2
        # now we can easily % and // by 10 to get digits
        # that would be reverse so add string backwards
        outstring = ""
        while res:
            digit = res % 10
            char = chr(ord('0') + digit)
            outstring = char + outstring
            res //= 10
        
        return outstring if outstring else '0'




        