class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # really clever way to solve this by recognizing must share a prefix at some point
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        if count:
            left <<= count
        return left

'''
# my first solution, brute force
        temp = left
        total = left
        while temp <= right:
            total &= temp
            temp += 1
        return total
'''
        