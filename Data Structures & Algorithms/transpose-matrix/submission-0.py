class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        trans = [[0 for _ in matrix] for _ in matrix[0]]

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i != j:
                    trans[j][i] = matrix[i][j]
                else:
                    trans[i][j] = matrix[i][j]

        return trans
        