class TrieNode:
    def __init__(self):
        self.child = {}
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.flag = True

    def search(self, word: str) -> bool:
        def dfs(word, root):
            node = root
            for index, c in enumerate(word):
                if c == '.':
                    for c in node.child:
                        res = dfs(word[index+1:], node.child[c])
                        if res:
                            return True
                    return False
                else:
                    if c not in node.child:
                        return False
                    node = node.child[c]
            return node.flag
        return dfs(word, self.root)
