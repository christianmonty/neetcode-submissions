class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # ok key here is need to do backtracking to generate the subsets. This is the "hard' part
        # here it's generate combinations, with duplicates
        # then XOR of eachsubset must be from a ^ b
        # then we just sum them up

        # do a thing, then recurse on. Then remove it and recurse again
        subsets = []

        def backtrack(index: int, s: Optional[List[int]]):
            # first we'll try no, then we will try adding it. Vs. add then remove it
            if index == len(nums):
                subsets.append(s.copy()) # want to add list at end of tentacles
                # s = []
                return
            
            s.append(nums[index])
            backtrack(index+1, s)
            s.remove(nums[index]) # should delete one occurence of item
            backtrack(index+1, s)
        

        backtrack(0, [])

        total = 0
        for s in subsets:
            print(s)
            subtotal = 0
            for i in s:
                subtotal ^= i
            total += subtotal
        
        return total







        