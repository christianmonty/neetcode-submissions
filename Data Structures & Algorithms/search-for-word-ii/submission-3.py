class TrieNode:
    def __init__(self, letter: str):
        self.letter = letter
        self.children = {}
        self.isWord = -1

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str, index: int):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.isWord = index # must mark final node with index of word in words
        # this is trickiest part of this problem, had to look up to grasp completely...


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        t = Trie()

        for index, word in enumerate(words):
            t.addWord(word, index)
        
        outlist = []
        visited = set()

        # tricky thing about this is keeping board position (i, j) separate from Trie position (node)
        def dfs(i: int, j: int, node: TrieNode):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited:
                return
            visited.add((i, j))
            if board[i][j] in node.children:
                node = node.children[board[i][j]]

                if node.isWord >= 0:
                    outlist.append(words[node.isWord])
                    node.isWord = -1

                dfs(i + 1, j, node)
                dfs(i - 1, j, node)
                dfs(i, j + 1, node)
                dfs(i, j - 1, node)            
            visited.remove((i, j))
            


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, t.root)
                '''
                firstlet = board[i][j]
                if firstlet in t.root.children:
                    dfs(i, j, t.root.children[firstlet])
                '''
        return outlist