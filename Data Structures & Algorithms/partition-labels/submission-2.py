from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # if two substrings contain same letter, must be merged inclusive, else do not merge

        # ok so we hash each letter into a list of indices where it resides
        # first letter, max is 2nd pointer (prev) or new [-1] furthest right
        # then go to all letters inside that string...
        # then have first, last, in between, and then j - i + 1 in output
        # then i = j + 1 and do it all again

        # this problem is greedy interval merge

        # greedy is taking the max for j
        hm = defaultdict(list)
        for index, c in enumerate(s):
            hm[c].append(index)
        
        i = 0
        outlist = []
        while i < len(s):
            let = s[i]
            j = hm[let][-1]
            k = i

            while k <= j:
                templet = s[k]
                newj = hm[templet][-1]
                if newj > j:
                    j = newj
                k += 1
            outlist.append(j - i + 1)
            i = j + 1
        
        return outlist



        