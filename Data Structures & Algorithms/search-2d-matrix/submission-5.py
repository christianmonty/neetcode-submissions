class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
        # row will be mid // row-length
        # column will be mid % row-length






        '''
        # first take median number of rows, and check target vs that. if less, move end backwards. If greater, move up front
        # then once top and bottom are same pointer, it's in that row (or doesn't exist). Do binary search again till joined, & return

        top, bot = 0, len(matrix) - 1

        while top < bot:
            if target < matrix[top][0] or target > matrix[bot][len(matrix[0]) - 1]:
                return False
            mid = (bot + top) // 2 # get this right - it's an average
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                top = mid + 1
            else:
                top = mid
                break
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right: # always check this
            mid = (right + left) // 2
            if matrix[top][mid] == target:
                return True
            if target < matrix[top][mid]:
                right = mid - 1
            else:
                left = mid + 1
    
        return False
        '''




































        '''
        #first we'll identify correct row, then call regular binary search on it

        rownum = len(matrix)
        count = rownum
        colnum = len(matrix[0])
        m = (rownum-1) // 2
        # add error check for empty lists
        def binS(l: int, r: int, row: int) -> int:
            if l > r:
                return False
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                return binS(mid+1, r, row)
            else:
                return binS(l, mid-1, row)

        while count > 0:
            if target < matrix[m][0]:
                if m > 0:
                    m -= 1
                    count -= 1
                else:
                    return False
            elif target > matrix[m][colnum-1]:
                if m < rownum - 1:
                    m += 1
                    count -= 1
                else:
                    return False
            else:
                break

        return binS(0, colnum-1, m)

        '''