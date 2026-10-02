class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def checkValid(arr: List[str]) -> bool:
            if not arr:
                return True # trivially true

            # below optimization I had to look up to not get infinite execution error when submitting...
            # this is optimized version, only need to check prior diagonal roles and columns above
            # invariant is rest of arr is already valid, just our new row that needs to be check
            r2 = len(arr) - 1
            c2 = arr[r2].index('Q')
            for r1 in range(r2):
                c1 = arr[r1].index('Q')
                if c1 == c2 or abs(r2 - r1) == abs(c2 - c1):
                    return False
            return True
            
            
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
        return len(outlist)