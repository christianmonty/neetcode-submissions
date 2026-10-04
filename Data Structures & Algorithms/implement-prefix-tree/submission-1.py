class TrieNode:
    def __init__(self, letter: str):
        self.letter = letter
        self.children = {}
        self.word = False

class PrefixTree:

    # for a Trie, we want to start with a specific letter, and it's children are next letter
    # so maybe we have a "dummy" sentinel node to start
    # each node should have a letter as value, and then a map of it's children, letter -> Trienode

    def __init__(self):
        self.root = TrieNode("") # for dummy sentinel node
        # make sure str vs. char works
        
    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children: 
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root

        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.word
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True
        