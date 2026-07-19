class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # make rotator of A-Z for each 26? (Keep modulo by 26?)
        # so every % 26 == 0 adds a Z

        outstring = ""
        num = columnNumber
        while num:
            num -= 1 # key to reduce this first since want 26 to be Z, NOT 0..
            digit = num % 26
            letter = chr(ord("A") + digit)
            outstring += letter
            num //= 26
        
        return ''.join(reversed(outstring))
