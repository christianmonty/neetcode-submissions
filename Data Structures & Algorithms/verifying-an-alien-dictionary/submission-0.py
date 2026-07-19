class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # two ideas for comparison: we can implement sorting to get O(nlogn) and then linear compare
        # or more easy to program we can compare O(n^2) times
        # and instinctively there may be another method as well

        hm = {}
        count = 0
        for o in order:
            hm[o] = count
            count += 1
        
        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                word1 = words[i]
                word2 = words[j]
                for idx, let in enumerate(word1): # get idx, val right!
                    if idx >= len(word2):
                        return False
                    if hm[word1[idx]] > hm[word2[idx]]:
                        return False
                    elif hm[word1[idx]] < hm[word2[idx]]:
                        break
        return True