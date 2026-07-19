class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
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