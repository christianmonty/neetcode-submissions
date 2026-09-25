class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # invariatn of mountain array is that target is one of either
        # the peak, left of peak, or right of peak

        # I guess one compication is peak not guaranteed to be at the middle
        # which means if peak left skew, say it's 8 at index 1, then 4 at index 4 and target
        # is 8 then you'd check right which would be wrong..
        # but if cell left of 4 is greater, check left. If cell left of 4 less then check right
        # since invariant is must be monotonically inc or dec, not ==.
        # ugh oh, what about if mid is the peak??
        # max 100 calls, 2^13.. * 2 so only 26 calls

        def binS(l: int, r: int) -> int:
            if l > r:
                return -1
            mid = (l + r) // 2
            res = mountainArr.get(mid) # first call
            if res == target:
                return mid
            if l == r:
                return -1
            left = mountainArr.get(mid - 1) # second call
            right = mountainArr.get(mid + 1) # third call
            if left == target:
                return mid - 1
            if left < res and right < res: # found peak!
                callleft = binS(l, mid - 1)
                callright = binS(mid + 1, r) # is there degenerate case here or only one peak?
                # could first try to find peak and then run this?
                if callleft != -1:
                    return callleft
                return callright
            else:
                if target > res:
                    if left < res:
                        # check to right of mid
                        return binS(mid + 1, r)
                    else:
                        # check to left of mid
                        return binS(l, mid - 1)
                elif target < res:
                    if left < res:
                        # check to left of mid
                        return binS(l, mid - 1)
                    else:
                        # check to right of mid
                        return binS(mid + 1, r)
        
        length = mountainArr.length()
        return binS(0, length - 1)