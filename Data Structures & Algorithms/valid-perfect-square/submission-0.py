class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        def recurse(l: int, r: int) -> bool:
            if l > r:
                return False
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                return recurse(mid + 1, r)
            else:
                return recurse(l, mid - 1)
        
        return recurse(0, num)
        
        