class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        minlen = min(len(word1), len(word2))
        newword = ""

        while i < minlen:
            newword += word1[i]
            newword += word2[i]
            i += 1
        
        if len(word1) > minlen:
            while i < len(word1):
                newword += word1[i]
                i += 1
        elif len(word2) > minlen:
            while i < len(word2):
                newword += word2[i]
                i += 1

        return newword
        