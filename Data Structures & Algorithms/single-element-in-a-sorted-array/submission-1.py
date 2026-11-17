class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # check middle, if prev or nxt is same, not middle
        # else check left half and right half
        # wait invariant is that middle (round down) should equal next. If it does not, 

        # two cases: even or odd length
        # if odd length, if middle is same as next element, must be in right half. else in left half
        # if even length, if two middles equal it's in right half, else in left half
        # wait then it always must be odd length...
        # [ 1 1 2 3    3        4 4 8 8]
        # [ 3 3 7      7          10 11 11]
        
        def recurse(l: int, r: int) -> int:
            if l > r or l < 0 or r > len(nums) - 1:
                return -1
            m = (l + r) // 2
            val = nums[m]
            if r - l == 0 or (m - 1 >= 0 and nums[m-1] != val and m + 1 < len(nums) and nums[m+1] != val):
                return val
            if m - 1 >= 0 and nums[m-1] == val:
                llen = m - 1 - l
                if llen % 2 != 0:
                    return recurse(l, m - 2)
                else:
                    return recurse(m+1, r)
            elif m + 1 < len(nums) and nums[m+1] == val:
                rlen = r - m + 1
                if rlen % 2 != 0:
                    return recurse(m + 2, r)
                else:
                    return recurse(l, m - 1)
        
        return recurse(0, len(nums) - 1)
            