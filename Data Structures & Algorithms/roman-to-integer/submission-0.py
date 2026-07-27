class Solution:
    def romanToInt(self, s: str) -> int:

        # one idea is we put everything in a hash map to convert
        # then we check if each thing is in hashmap, except I are singletons. Oh wait we can just add

        hm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        # if there are more than one left, first see if two are in hm, if so take that and advanced two. Else, take 1 & advance once
        sumn = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in hm:
                sumn += hm[s[i:i+2]]
                i += 2
            else:
                sumn += hm[s[i]]
                i += 1
    
        return sumn
        