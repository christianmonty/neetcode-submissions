from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # brute force: first letter of all workds is an order
        # then if first letter equal, second letter is an order
        # how can we do this in a graph? Dependency list maybe...
        # let's try to think of a Djkstra's -> shortest path one node to all

        # oh wait the top sort version is starting with letters of indegree 0
        # O(n^2) to compare all words & O(w) len longest word
        # if first letters differ, indegree[right] += 1. hm[left].append(right)
        # if not empty / found cycle then return ""
        # if right word prefix of left but shorter, return ""
        # how to check if prefix efficiently? Oh if at end of letters of b but a continues on...if b not empty

        hm = defaultdict(set)
        indeg = {c: 0 for w in words for c in w} # weird syntax to initialize as 0
        q = deque()
        used = set()

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word1 = words[i]
                word2 = words[j]
                for index in range(len(word1)):
                    if index >= len(word2):
                        return "" # impossible
                    l = word1[index]
                    r = word2[index]
                    if l != r:
                        if r not in hm[l]:
                            hm[l].add(r) # set ignores duplicates
                            indeg[r] += 1
                        break

        # now we have all the causal relationships formed
        for key, val in indeg.items():
            if val == 0:
                q.append(key)

        outstring = []
        while q:
            nextlet = q.popleft()
            if nextlet in used:
                return ""
            used.add(nextlet)
            outstring.append(nextlet)
            for depend in hm[nextlet]:
                indeg[depend] -= 1
                if indeg[depend] == 0:
                    q.append(depend)

        res = "".join(outstring)
        return res if len(indeg) == len(res) else ""
            


        