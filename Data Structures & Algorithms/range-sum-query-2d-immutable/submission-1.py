class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # init can take longer, since matrix is 
        self.arr = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                self.arr[i][j] = matrix[i][j]
                if j > 0:
                    self.arr[i][j] += self.arr[i][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # this must respond in O(1) time with sumRegion
        ssum = 0
        # prefix array instead of sum array

        for i in range(row1, row2 + 1):
            start = 0 if col1 == 0 else self.arr[i][col1 - 1]
            ssum += self.arr[i][col2] - start
        return ssum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# one idea is to use prefix sum (per hint)
# so could have each row, represent a 1D prefix sum for that thing
# and then for square, do for i from row1 to row2: += prefix[i][col2] - prefix[i][col1 - 1]
# or if col1 is < 0 then make it 0 so subtract nothing