class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        firstlet = word[0]

        def isV(row: int, col: int) -> bool:
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            return True

        def checkN(subword: str, m: int, n: int, h: set) -> bool:
            if not subword or len(subword) == 1:
                return True
            letter = subword[1]
            res1 = res2 = res3 = res4 = False
            if isV(m-1, n):
                if board[m-1][n] == letter and (m-1, n) not in h:
                    newh = h.copy()
                    newh.add((m-1, n))
                    res1 = checkN(subword[1:], m-1, n, newh)
            if isV(m+1, n):
                if board[m+1][n] == letter and (m+1, n) not in h:
                    newh = h.copy()
                    newh.add((m+1, n))
                    res2 = checkN(subword[1:], m+1, n, newh)
            if isV(m, n-1):
                if board[m][n-1] == letter and (m, n-1) not in h:
                    newh = h.copy()
                    newh.add((m, n-1))
                    res3 = checkN(subword[1:], m, n-1, newh)
            if isV(m, n+1):
                if board[m][n+1] == letter and (m, n+1) not in h:
                    newh = h.copy()
                    newh.add((m, n+1))
                    res4 = checkN(subword[1:], m, n+1, newh)
            return res1 or res2 or res3 or res4

        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == firstlet:
                    hs = set()
                    hs.add((i, j))
                    res = checkN(word, i, j, hs)
                    if res:
                        return True
        return False


