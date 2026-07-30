class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # two immediate approaches are try to convert to binary, add then convert back to string
        # or try to add while still strings. Given bit manipulation category, assume that it's that. 

        # one idea is we literally do it digit by digit so whichever one is shorter, start with higher digit?
        # and then propagate carry to MSD, then go to next digit and do the same, and finally ones digit
        # maybe define a "binary add" function for each digit
        # but if we're supposed to do bit manipulation there must be a cleaner way
        
        # one idea is go from back to front of both strings, account for the carry etc.
        # then when have the answer as an array (or reversed) then convert to string. But where is bit manipulation?
        
        # from solution: clever to reverse both strings first, with a carry of 0
        # had to look up solution to verify no bit manipulation needed, implemented on my own

        a = a[::-1]
        b = b[::-1]

        carry = 0
        res = ""

        maxlen = max(len(a), len(b))

        for i in range(maxlen):
            dig1 = dig2 = 0
            if i < len(a):
                dig1 = int(a[i])
            if i < len(b):
                dig2 = int(b[i])
            total = carry + dig1 + dig2
            res += str(total % 2)
            carry = total // 2
        if carry:
            res += str(carry)
        
        return res[::-1]