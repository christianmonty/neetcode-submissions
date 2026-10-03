from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # since it's graph problem, for min length traversal I like BFS in queue could stoere tuple
        # with level accordingly
        # question is how to propose switching letters it's be O(l * 26) and wasted stuck
        # or we could also think about Djkstra's? Shortest path from one node to another


        hs = set(wordList)
        done = set()
        # guess we should remove from set once popped from queue
        q = deque()
        q.append((beginWord, 1))

        while q:
            nextWord, layer = q.popleft()
            if nextWord == endWord:
                return layer
            done.add(nextWord)
            for i in range(len(beginWord)):
                for j in range(0, 27):
                    temp = nextWord
                    newWord = nextWord[:i] + chr(ord('a') + j) + nextWord[i+1:]
                    if newWord in hs and newWord not in done:
                        q.append((newWord, layer + 1))
                    nextWord = temp
        return 0



        