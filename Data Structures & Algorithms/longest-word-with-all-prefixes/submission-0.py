class TrieNode:
    def __init__(self):
        self.neighbors = {}
        self.word = False
        # don't actually need to store the letters in the neighbors map

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        for w in word:  
            if w not in node.neighbors:
                node.neighbors[w] = TrieNode()
            node = node.neighbors[w]
        node.word = True

    def checkWord(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.neighbors:
                return False
            node = node.neighbors[w]
            if not node.word:
                return False
        return node.word
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        T = Trie()
        longest = ""
        for w in words:
            T.addWord(w)
        for w in words:
            if T.checkWord(w):
                if len(w) > len(longest):
                    longest = w
                if len(w) == len(longest) and w < longest:
                    longest = w
        
        return longest


