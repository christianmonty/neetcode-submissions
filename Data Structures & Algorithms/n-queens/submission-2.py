class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # note from example 1 the board is flipped vertically (or the pieces are) and it works
        # thinking about brute force, could go row by row, place Q, recurse to next row, then remove, recurse
        # and in each layer, try playing of four times and recursing
        # once get to final layer (or at any layer) run queencheck function which checks if valid
        # if place final layer and queen check is valid, return 1, else invalid return 0
        # then accumulate across trying all 4 queen places each level
        # since n can only be up to 8 levels, does that limit to only 8 layer recursion? Yes but forking 8 per

        # so ideally we check valid each time since oply O(1) in 64 checks? and limits recursive branching...

        def checkValid(arr: List[str]) -> bool:
            if not arr:
                return True # trivially true

            # this is optimized version, only need to check prior diagonal roles and columns above
            # invariant is rest of arr is already valid, just our new row that needs to be check
            r2 = len(arr) - 1
            c2 = arr[r2].index('Q')
            for r1 in range(r2):
                c1 = arr[r1].index('Q')
                if c1 == c2 or abs(r2 - r1) == abs(c2 - c1):
                    return False
            return True
            
            '''
            # below is brute force checkValid but need to optimize it...

            # row build can't fail, since we construct it
            
            for col, val in enumerate(arr[0]):
                count = 0
                for row, value in enumerate(arr):
                    if arr[row][col] == 'Q':
                        count += 1
                if count > 1:
                    return False

            # my idea for checking validity of diagonals
            startingcols = [(0, i) for i in range(n)]
            startingrows = [(i, 0) for i in range(1, len(arr))]
            starts = startingcols + startingrows

            for sr, sc in starts:
                count = 0
                while sr < len(arr) and sc < n:
                    if arr[sr][sc] == 'Q':
                        count += 1
                    sr += 1
                    sc += 1
                if count > 1:
                    return False

            # also have to check top right to bottom left diagonals....!
            antidiag = [(0, i) for i in range(n)] + [(i, n-1) for i in range(1, len(arr))]

            for sr, sc in antidiag:
                count = 0
                while sr < len(arr) and sc >= 0:
                    if arr[sr][sc] == 'Q':
                        count += 1
                    sr += 1
                    sc -= 1
                if count > 1:
                    return False

            return True
            '''


        def recurse(board: List[str]):
            if not checkValid(board):
                return

            if len(board) == n:
                outlist.append(board.copy()) # key to .copy() to freeze snapshot
                return
            
            for i in range(n):
                text = '.' * i + 'Q' + '.' * (n - 1 - i)
                board.append(text)
                recurse(board)
                board.pop()
            


        outlist = []
        recurse([])
        return outlist