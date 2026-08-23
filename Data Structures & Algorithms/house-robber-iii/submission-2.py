# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # I figured out on pen/paper that want to always return best val using cur node vs. not using it

        # start bottom up if no children return self and activated!
        def checkMax(node: TreeNode) -> (int, int):
            if not node.left and not node.right: # if Leaf, return current value
                return node.val, 0 # this is return if True, then if False

            selfsum = node.val
            truechildsum = 0
            LTrue = LFalse = RTrue = RFalse = 0

            if node.left:
                LTrue, LFalse = checkMax(node.left)
            if node.right:
                RTrue, RFalse = checkMax(node.right)
            
            truechildsum = max(LTrue + RTrue, LTrue + RFalse, LFalse + RTrue, LFalse + RFalse)
            selfsum += (LFalse + RFalse)

            return selfsum, truechildsum # best return from using cur, vs. not using cur

        useRoot, skipRoot = checkMax(root)
        return max(useRoot, skipRoot)


        
        # pattern I noticed, say 3 does 2 recursive calls on children, can take 4 + 2 or 3, choose 4 + 2 into 6 but False (not activate)
        # then basically 2 compares to 5 activated vs. 2, take 5 and then must return inactive, can take 6.
        # then 1 gets returned an inactive, can take itself for free

        # wait idk if greedy will work here...need to see parent visibility...?.........................

        # ultimately, at each step, need to decide whether to skip the house and rob the next, or rob the house
        # this sounds like DP. This is for max money. 
        # so like in example 2, get to leaf, return val and yes
        # then when processing, choose to either take sum of leaves OR self
        # when 3 returns No, 6 and 5 returns yes, 5, 2 decides do I take self + any no's or do I not take Self, and at least one yes
        # then when get to root, returns 11, no then 1 takes 11 + 1 = 12. 
        # if don't take self, obviously return No. If take self must return yes

        