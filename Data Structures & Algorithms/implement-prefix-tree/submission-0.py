class TrieNode:
    def __init__(self):
        self.child = {}
        self.flag = False
#Have to know to build above Node conceptually

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.flag = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]
        return node.flag

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        last = prefix[len(prefix)-1]
        for c in prefix:
            if c not in node.child:
                return False
            elif c == last:
                return True
            else:
                node = node.child[c]
            
        