class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hs = set(wordDict) # check if works

        outlist = []
        outset = set()

        # we need to try spaces at every point? len(s) space options, but which ones to keep?
        # maybe first we try each space


        
        def recurse(substring: str) -> List[str]:
            if substring == "":
                return []
            
            outputlist = []
            for i in range(len(substring)):
                word = substring[0:i + 1]
                if word in wordDict:
                    retlist = recurse(substring[i + 1:]) # slicing never returns empty string!
                    
                    if not retlist and i == len(substring) - 1:
                        outputlist.append(word)
                    for lis in retlist:
                        output = word + " " + lis
                        outputlist.append(output)
            return outputlist


        ret = recurse(s)
        outlist = []
        for res in ret:
            if res not in outset:
                outlist.append(res)
                outset.add(res)
        
        return outlist
                


        