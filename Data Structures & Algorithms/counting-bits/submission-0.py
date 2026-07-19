class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = []

        for i in range(0, n+1):
            p = i

            count = 0
            while p:
                res = p & 1
                count += res
                p >>= 1
            result.append(count)
        
        return result