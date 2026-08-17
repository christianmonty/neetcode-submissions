class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # one thing you can do is surround the matrix with larger matrix that has zeroes
        # define four directions as four states. While you don't hit a zero, keep going. If hit zero change state
        # stopping condition is if you can't make next move since 0 in new direction there, return output then

        # this is one of those ones that takes a little time to, but is fun to code up

        # TBD: build duplicate matrix with zeroes at every end
        newm = [[101 for _ in range(len(matrix[0]) + 2)] for _ in range(len(matrix) + 2)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newm[i+1][j+1] = matrix[i][j]
        
        i = j = 1
        # below goes right, down, left, up with i as row, j as col
        dirs = [[0,1], [1,0], [0,-1], [-1, 0]]
        k = 0
        outlist = []
        while True:
            outlist.append(newm[i][j])
            newm[i][j] = 101 # must set to 101 after visited
            if newm[i + dirs[k][0]][j + dirs[k][1]] == 101: # if can't move anymore
                # change direction
                k = (k + 1) % 4
                if newm[i + dirs[k][0]][j + dirs[k][1]] == 101:
                    break # we're done
            i += dirs[k][0]
            j += dirs[k][1]
        
        return outlist

