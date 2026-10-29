class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        outlist = []
        beg = 0

        for space in spaces:
            outlist.append(s[beg:space])
            outlist.append(" ")
            beg = space
        outlist.append(s[beg:])
        



        '''
        hs = set(spaces)
        for ind, val in enumerate(s):
            if ind in spaces:
                outlist.append(" ")
            outlist.append(val)
        '''
        
        return "".join(outlist)