class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #one idea is do a bunch of iterations across 9 rows, then 9 columns, then 9 boxes. Start new ht for each
        #if any already in ht, return false. Except '.'
        i = 0
        j = 0
        size = 9

        for i in range(0, size):
            hi = set()
            for j in range(0, size):
                item = board[i][j]
                if item not in hi:
                    hi.add(item)
                elif item in hi and item != '.':
                    return False
                j += 1
            i += 1
        
        for j in range(0, size):
            hj = set()
            for i in range(0, size):
                item = board[i][j]
                if item not in hj:
                    hj.add(item)
                elif item in hj and item != '.':
                    return False
                i += 1
            j += 1

        #if either i % 3 == 0 or j % 3 == 0
        box = [[0,0], [0, 3], [0, 6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for k in range(0, 9):
            hmb = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    item = board[i+box[k][0]][j+box[k][1]]
                    if item not in hmb:
                        hmb.add(item)
                    elif item in hmb and item != '.':
                        return False
                    j += 1
                i += 1
            k += 1
        
        return True

        