class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            sortchar = sorted(string);
            sortstring = ''.join(sortchar)
            if sortstring in d:
                d[sortstring].append(string)
            else:
                d[sortstring] = [string]
        
        outputlist = []
        for strings in d:
            outputlist.append(d[strings])
        return outputlist