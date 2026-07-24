class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # unique means hashset or map
        # PRACTICE AGAIN FULL THING FROM SCRATCH, would not have known how to do this

        # maybe we need a for loop where we put each first, and then what?
        # key to backtracking is loop inside recursive function

        hs = set()

        def permute(i : int, sub: List[int]):
            # i must be where source from, j is where place
            if i == len(nums):
                tup = tuple(sub.copy()) # must copy here, cannot take by reference?
                if tup not in hs:
                    hs.add(tup)
                return
            
            for j in range(0, len(sub)+1): # each index to place it.
            # change to len(sub) + 1
                sub.insert(j, nums[i])
                permute(i+1, sub)
                sub.pop(j)
        
        permute(0, [])
        outlist = []
        for s in hs:
            outlist.append(list(s))
        return outlist