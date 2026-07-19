class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # I wouldn't have seen trick to vertically flip, then transpose

        ROWS, COLS = len(matrix), len(matrix[0])
        n = ROWS - 1
        for i in range(ROWS//2):
            for j in range(COLS):
                temp = matrix[n - i][j]
                matrix[n-i][j] = matrix[i][j] 
                matrix[i][j] = temp
        
        for i in range(ROWS):
            for j in range(i, COLS):
                if i != j:
                    temp = matrix[j][i]
                    matrix[j][i] = matrix[i][j]
                    matrix[i][j] = temp
        
        '''for i in range(ROWS//2):
            temp = matrix[n-i][n-i]
            matrix[n-i][n-i] = matrix[i][i]
            matrix[i][i] = temp
        '''
        
        
