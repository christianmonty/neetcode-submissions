class TrieNode:
    def __init__(self):
        self.words = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        temp = self.root
        temp.count += 1
        for w in word:
            if w not in temp.words:
                temp.words[w] = TrieNode()
            temp = temp.words[w] # move to that node
            temp.count += 1
        # temp.isWord = True

    def checkPrefix(self, prefix: str) -> int:
        temp = self.root
        for p in prefix:
            if p not in temp.words:
                return 0
            temp = temp.words[p]
        return temp.count


# should we have both Trie class and TrieNode class? TrieNode to store if state is word



class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        root = Trie()
        for word in words:
            root.addWord(word)

        return root.checkPrefix(pref)
        



        