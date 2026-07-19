class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board) - 1
        cols = len(board[0]) - 1
        directions = [[-1, 0], [1,0], [0, 1], [0,-1]]
        ghs = set()
        ll = []
        
        def checkreg(i: int, j: int) -> str:
            if i < 0 or i > rows or j < 0 or j > cols:
                return 'O'
            elif board[i][j] == 'X':
                return 'X'

            ghs.add((i, j))
            ll.append([i, j])
            found = 'X'
            for d in directions:
                a = d[0] + i
                b = d[1] + j
                if (a, b) not in ghs:
                    res = checkreg(a, b)
                    if res == 'O':
                        found = 'O'
            return found

        for i in range(0, rows):
            for j in range(0, cols):
                if (i, j) not in ghs and board[i][j] == 'O':
                    ll = []
                    res = checkreg(i, j)
                    if res == 'X':
                        for tup in ll:
                            board[tup[0]][tup[1]] = 'X'

        
        