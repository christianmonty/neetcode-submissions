class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # the trick is you start with first index fixed, skipping duplicates
        # then second index fixed from their iterating to end
        # then do two pointers within to go from O(n^4) -> O(n^3)

        nums.sort()
        hm = set()

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1 # might have to remove break
                continue
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    quad = [nums[i], nums[j], nums[k], nums[l]]
                    ssum = sum(quad)

                    if ssum == target:
                        if tuple(quad) not in hm:
                            hm.add(tuple(quad))
                        k += 1
                        l -= 1
                    elif ssum < target:
                        k += 1
                    else:
                        l -= 1
        
        outlist = []
        for q in hm:
            temp = [q[0], q[1], q[2], q[3]]
            outlist.append(temp)
        return outlist



        '''
        # THIS WAS A SUPER CREATIVE FIRST ATTEMPT, BUT MISSES SOME VS. 2 LOOPS W/2 POINTERS WIHTIN
        # WAS REALLY COOL I TRIED TO MOVE INWARDS BY POS/NEG BUT CAN DO SIMPLER, in O(n^3)
        # seems similar to three sum, except solving for sum == target instead of 0
        # maybe we have l and r in mid and back and front on edges
        nums.sort()
        if len(nums) < 4:
            return []

        back, front = 0, len(nums) - 1
        hm = set()
        
        while front - back >= 3:
            l, r = back + 1, front - 1

            while l < r:
                quad = [nums[back], nums[l], nums[r], nums[front]]
                quad.sort()
                ssum = sum(quad)
                
                # if too big, move left and right in. If too small, move front forward
                if ssum == target:
                    if tuple(quad) not in hm:
                        hm.add(tuple(quad))
                    r -= 1
                    l += 1
                elif ssum > target:
                    r -= 1
                else:
                    l += 1
            if (l - back) >= (front - r):
                back += 1
            else:
                front -= 1



        outlist = []
        for q in hm:
            temp = [q[0], q[1], q[2], q[3]]
            outlist.append(temp)
        return outlist
        '''

