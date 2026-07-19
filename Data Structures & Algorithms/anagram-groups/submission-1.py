class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}

        for s in strs:
            sorts = sorted(list(s))
            key = "".join(sorts)

            if key in hm:
                newlist = list(hm[key])
                newlist.append(s)
                hm[key] = tuple(newlist)
            else:
                hm[key] = tuple([s])

        outlist = []
        for index in hm:
            temptup = hm[index]
            outlist.append(list(temptup))

        return outlist