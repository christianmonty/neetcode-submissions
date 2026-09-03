class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # have solved once already, practing this again to intuit greedy pattern again

        # when I think greedy, I think always take the max jump length? But clearly, shorter jump may be optiomal
        # problem if this misses jumping over larger better jumps ofc
        # maybe there is way that if we're mid jump, jumping over higher number, just take that...
        # but does that fail final test case with tons of 2 jumps. Either way must iterate over O(n) I think


        # Maybe we don't need recursion altogether, nums.length of 1000 or less so can easily iterate
        power = 0
        if len(nums) == 1:
            return True # trivially True
    
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == 0:
                    return False
                else:
                    power += nums[i]
            else:
                power -= 1
                if power <= 0 and nums[i] == 0 and i != len(nums) - 1:
                    return False
                elif nums[i] > power:
                    power = nums[i]
        return True



    '''
        def recurse(index: int) -> bool:
            if index >= len(nums) - 1:
                return True
            maxJump = nums[index]

            # if not maxJump:
                # return False

            # return recurse(index + maxJump)

            for i in range(1, maxJump + 1):
                ret = recurse(index + i)
                if ret:
                    return True
            return False

        return recurse(0)
    '''